from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, Group
from django.db import models
from django.utils import timezone
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField

from policy.models import Room


class School(models.Model):
    name = models.CharField(
        max_length=100,
    )
    country = CountryField()

    def __str__(self):
        return self.name


class UserGroup(Group):
    pass


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, is_staff, is_superuser, **extra_fields):
        if not email:
            raise ValueError('The email must be set')
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            is_staff=is_staff,
            is_active=True,
            is_superuser=is_superuser,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        return self._create_user(email, password, False, False, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        return self._create_user(email, password, True, True, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Others'),
    ]

    is_staff = models.BooleanField(
        verbose_name='staff status',
        default=False,
        help_text='Designates whether the user can log into this admin site.',
    )
    is_active = models.BooleanField(
        verbose_name='active',
        default=True,
        help_text='Designates whether this user should be treated as active. '
                  'Unselect this instead of deleting accounts.',
    )
    groups = models.ManyToManyField(
        to=UserGroup,
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to. A user will ' 
                  'get all permissions granted to each of their groups.',
        related_name='user_set',
        related_query_name='user',
    )
    date_joined = models.DateTimeField(
        verbose_name='date joined',
        default=timezone.now,
    )

    email = models.EmailField(
        verbose_name='email address',
        unique=True,
        error_messages={
            'unique': 'A user with that username already exists.',
        },
    )
    first_name = models.CharField(
        max_length=30,
    )
    last_name = models.CharField(
        max_length=30,
    )
    birthday = models.DateField(
        null=True,
    )
    nationality = CountryField(
        null=True,
    )
    gender = models.CharField(
        max_length=1,
        choices=GENDER_CHOICES,
        null=True,
    )
    phone_number = PhoneNumberField(
        null=True,
    )
    school = models.ForeignKey(
        to=School,
        on_delete=models.PROTECT,
        blank=True,
        null=True,
    )
    major = models.CharField(max_length=100)

    assigned_room = models.ForeignKey(
        to=Room,
        related_name='users',
        blank=True,
        null=True,
    )

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def get_full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)

    def get_short_name(self):
        return self.first_name

    def __str__(self):
        return self.get_full_name()
