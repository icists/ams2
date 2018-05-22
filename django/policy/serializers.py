from rest_framework.serializers import ModelSerializer

from .models import Stage, PaymentInfo, Price, AccommodationOption, EssayTopic, ProjectTopic


class StageSerializer(ModelSerializer):
    class Meta:
        model = Stage
        fields = (
            'current_stage',
        )


class PaymentInfoSerializer(ModelSerializer):
    class Meta:
        model = PaymentInfo
        exclude = (
            'id',
        )


class PriceSerializer(ModelSerializer):
    class Meta:
        model = Price
        fields = (
            'id',
            'code',
            'description',
            'price_krw',
            'price_usd',
        )


class AccommodationOptionSerializer(ModelSerializer):
    class Meta:
        model = AccommodationOption
        fields = (
            'id',
            'code',
            'description',
            'price_krw',
            'price_usd',
            'capacity',
        )


class EssayTopicSerializer(ModelSerializer):
    class Meta:
        model = EssayTopic
        fields = (
            'number',
            'title',
            'description',
        )


class ProjectTopicSerializer(ModelSerializer):
    class Meta:
        model = ProjectTopic
        fields = (
            'number',
            'title',
        )
