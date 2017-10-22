from django.db import models
from django.core.exceptions import ValidationError


def swift_code_validator(code):
    code_length = len(code)
    if code_length not in [8, 11]:
        raise ValidationError('Swift code must have 8 or 11 characters.')


class Stage(models.Model):
    STAGES = [
        ('BE', 'Before Early'),
        ('ES', 'Early'),
        ('EC', 'Early Closed'),
        ('RS', 'Regular'),
        ('RC', 'Regular Closed'),
        ('LS', 'Late'),
        ('LC', 'Late Closed'),
    ]

    name = models.CharField(max_length=2, choices=STAGES)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    # TODO: Check conflict between stages


class Price(models.Model):
    code = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=100)
    krw = models.PositiveIntegerField(verbose_name='in KRW')
    usd = models.PositiveIntegerField(verbose_name='in USD')

    def __str__(self):
        return self.description


class AccommodationOption(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    capacity = models.PositiveSmallIntegerField()
    num_rooms = models.PositiveSmallIntegerField(verbose_name='number of rooms')
    price_krw = models.PositiveIntegerField(verbose_name='price in KRW')
    price_usd = models.PositiveIntegerField(verbose_name='price in USD')

    def __str__(self):
        return '{} (Capacity: {})'.format(self.name, self.capacity)

    def get_total_capacity(self):
        return self.capacity * self.num_rooms


class PaymentInfo(models.Model):
    bank_name = models.CharField(max_length=100)
    bank_branch = models.CharField(max_length=100)
    account_number = models.CharField(max_length=30)
    recipient = models.CharField(max_length=50)
    swift_code = models.CharField(max_length=11, validators=[swift_code_validator])

    def __str__(self):
        return '{} ({})'.format(self.recipient, self.bank_name)
