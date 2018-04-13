from django.core.exceptions import ObjectDoesNotExist
from django.utils.encoding import smart_text
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from policy.models import AccommodationOption, Price
from .models import Application, Order, Group


class CreatableSlugRelatedField(serializers.SlugRelatedField):
    def to_internal_value(self, data):
        try:
            return self.get_queryset().get_or_create(**{self.slug_field: data})[0]
        except ObjectDoesNotExist:
            self.fail('does_not_exist', slug_name=self.slug_field, value=smart_text(data))
        except (TypeError, ValueError):
            self.fail('invalid')


class ApplicationSerializer(ModelSerializer):
    screening_result = serializers.CharField(
        source='get_screening_result',
        read_only=True
    )

    group = CreatableSlugRelatedField(
        slug_field='name',
        queryset=Group.objects.all()
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
