from rest_framework.serializers import ModelSerializer

from .models import School, User


class SchoolSerializer(ModelSerializer):
    class Meta:
        model = School
        fields = (
            'name',
            'country',
        )


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        exclude = (
            'id',
            'password',
            'groups',
            'date_joined',
            'user_permissions',
        )
