from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import Application, Order


class SimpleApplicationSerializer(ModelSerializer):
    screening_result = serializers.CharField(source='get_screening_result')

    class Meta:
        model = Application
        fields = (
            'id',
            'stage',
            'screening_result',
        )


class ApplicationSerializer(ModelSerializer):
    screening_result = serializers.CharField(source='get_screening_result')

    class Meta:
        model = Application
        exclude = (
            'id',
            'user',
            'last_update',
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
