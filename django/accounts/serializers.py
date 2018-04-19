import logging

from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email
from django_countries.serializer_fields import CountryField
from phonenumber_field.serializerfields import PhoneNumberField
from rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers

from .models import School, User

logger = logging.getLogger(__name__)


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = (
            'id',
            'name',
            'country',
        )


class CountrySerializer(serializers.Serializer):
    code = serializers.CharField()
    name = serializers.CharField()


class UserRegisterSerializer(RegisterSerializer):
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    birthday = serializers.DateField(required=True)
    nationality = CountryField(required=True)
    phone_number = PhoneNumberField(required=True)
    school = serializers.PrimaryKeyRelatedField(queryset=School.objects.all(), required=True)
    gender = serializers.CharField(required=True)

    def get_cleaned_data(self):
        logger.warning("data : {}".format(self.validated_data))

        return {
            'email': self.validated_data.get('email', ''),
            'first_name': self.validated_data.get('first_name', ''),
            'last_name': self.validated_data.get('last_name', ''),
            'password1': self.validated_data.get('password1', ''),
        }

    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()

        user.birthday = self.validated_data.get('birthday', '')
        user.nationality = self.validated_data.get('nationality', '')
        user.phone_number = self.validated_data.get('phone_number', '')
        user.school = self.validated_data.get('school', '')
        user.gender = self.validated_data.get('gender', '')

        adapter.save_user(request, user, self)
        self.custom_signup(request, user)
        setup_user_email(request, user, [])
        return user

    class Meta:
        model = User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    id = serializers.IntegerField(read_only=True)
    nationality = CountryField(required=True)

    def create(self, validated_data):
        User.objects.create_user(validated_data['email'], validated_data['password'], validated_data)

    class Meta:
        model = User
        exclude = (
            'groups',
            'date_joined',
            'user_permissions',
            'is_superuser',
            'is_staff',
            'is_active',
        )
