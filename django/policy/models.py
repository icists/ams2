from django.core.exceptions import ValidationError
from django.db import models
from solo.models import SingletonModel


def swift_code_validator(code):
    code_length = len(code)
    if code_length not in [8, 11]:
        raise ValidationError('Swift code must have 8 or 11 characters.')


class Stage(SingletonModel):
    STAGES = [
        ('BE', 'Before Early'),
        ('EO', 'Early Open'),
        ('EC', 'Early Closed'),
        ('RO', 'Regular Open'),
        ('RC', 'Regular Closed'),
        ('LO', 'Late Open'),
        ('LC', 'Late Closed'),
    ]

    current_stage = models.CharField(max_length=2, choices=STAGES)

    class Meta:
        verbose_name = 'application stage'


class AbstractOption(models.Model):
    code = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=100)
    price_krw = models.PositiveIntegerField(verbose_name='price in KRW')
    price_usd = models.PositiveIntegerField(verbose_name='price in USD')

    def __str__(self):
        return self.description

    class Meta:
        abstract = True


class Price(AbstractOption):
    pass


class AccommodationOption(AbstractOption):
    capacity = models.PositiveSmallIntegerField()
    num_rooms = models.PositiveSmallIntegerField(verbose_name='number of rooms')

    def get_total_capacity(self):
        return self.capacity * self.num_rooms


class Room(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Others'),
    ]

    type = models.ForeignKey(AccommodationOption)
    number = models.PositiveSmallIntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    def __str__(self):
        return '{} #{} ({})'.format(self.type.description, self.number, self.gender)

    def occupied_seats(self):
        return self.users.count()

    def full_capacity(self):
        return self.type.capacity


class PaymentInfo(SingletonModel):
    bank_name = models.CharField(max_length=100)
    bank_branch = models.CharField(max_length=100)
    account_number = models.CharField(max_length=30)
    recipient = models.CharField(max_length=50)
    swift_code = models.CharField(max_length=11, validators=[swift_code_validator])

    class Meta:
        verbose_name = 'payment information'
