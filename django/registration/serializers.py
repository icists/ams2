from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import Application, Order

class SimpleApplicationSerializer(ModelSerializer):
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
            'essay_topic'
        )


class ApplicationSerializer(ModelSerializer):
    screening_result = serializers.CharField(
        source='get_screening_result',
        read_only=True
    )

    class Meta:
        model = Application
        exclude = (
            'id',
            'user',
            'last_update',
        )

class SimpleOrderSerializer(ModelSerializer):

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

class OrderSerializer(ModelSerializer):
    accommodation = serializers.PrimaryKeyRelatedField(
        read_only=True,
    )
    options = serializers.PrimaryKeyRelatedField(
        many=True,
        read_only=True,
    )

    class Meta:
        model = Order
        fields = (
            'preferred_currency',
            'paid_amount',
            'accommodation',
            'options',
            'dietary_preferences',
        )
