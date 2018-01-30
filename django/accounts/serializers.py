from rest_framework.serializers import ModelSerializer
from django_countries.serializer_fields import CountryField

from .models import School, User


class SchoolSerializer(ModelSerializer):
    class Meta:
        model = School
        fields = (
            'name',
            'country',
        )


class UserSerializer(ModelSerializer):
    nationality = CountryField()

    class Meta:
        model = User
        exclude = (
            'id',
            'password',
            'groups',
            'date_joined',
            'user_permissions',
        )
