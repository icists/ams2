from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import Application, Order
from policy.models import AccommodationOption, Price


class ApplicationSerializer(ModelSerializer):
    screening_result = serializers.CharField(
        source='get_screening_result',
        read_only=True
    )

    class Meta:
        model = Application
        fields = (
            'id',
            'stage',
            'screening_result',
            'topic_preference',
            'essay_topic',
            'essay_text',
            'group',
            'visa_letter',
            'financial_aid',
            'previous_participation',
        )
        read_only_fields = (
            'id',
            'stage',
        )


class OrderSerializer(ModelSerializer):
    accommodation = serializers.PrimaryKeyRelatedField(
        queryset=AccommodationOption.objects.all(),
    )
    options = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Price.objects.all(),
    )

    class Meta:
        model = Order
        fields = (
            'id',
            'preferred_currency',
            'paid_amount',
            'accommodation',
            'options',
            'dietary_preferences',
        )
        read_only_fields = (
            'id',
            'paid_amount',
        )
