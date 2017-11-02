from django.core.exceptions import ValidationError
from django.db import models
from django.utils.deconstruct import deconstructible
from djmoney.models.fields import MoneyField
from solo.models import SingletonModel


def swift_code_validator(code):
    code_length = len(code)
    if code_length not in [8, 11]:
        raise ValidationError('Swift code must have 8 or 11 characters.')


@deconstructible
class CurrencyValidator(object):
    def __init__(self, currency):
        self.currency = currency

    def __call__(self, money):
        if money.currency.code != self.currency:
            raise ValidationError('Please check the currency.')


class Stage(SingletonModel):
    BEFORE_EARLY, EARLY, EARLY_CLOSED = 'BE', 'E', 'EC'
    REGULAR, REGULAR_CLOSED, LATE, LATE_CLOSED = 'R', 'RC', 'L', 'LC'
    STAGES = [
        (BEFORE_EARLY, 'Before Early'),
        (EARLY, 'Early'),
        (EARLY_CLOSED, 'Early Closed'),
        (REGULAR, 'Regular'),
        (REGULAR_CLOSED, 'Regular Closed'),
        (LATE, 'Late'),
        (LATE_CLOSED, 'Late Closed'),
    ]

    current_stage = models.CharField(max_length=2, choices=STAGES, default=BEFORE_EARLY)

    def get_current_stage(self):
        return self.current_stage

    class Meta:
        verbose_name = 'application stage'


class AbstractOption(models.Model):
    code = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=100)
    price_krw = MoneyField('price in KRW', max_digits=7, decimal_places=0, default=0, default_currency='KRW',
                           validators=[CurrencyValidator('KRW')])
    price_usd = MoneyField('price in USD', max_digits=4, decimal_places=0, default=0, default_currency='USD',
                           validators=[CurrencyValidator('USD')])

    def __str__(self):
        return self.description

    class Meta:
        abstract = True


class Price(AbstractOption):
    pass


class AccommodationOption(AbstractOption):
    capacity = models.PositiveSmallIntegerField()
    num_rooms = models.PositiveSmallIntegerField('number of rooms')

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


class Configuration(SingletonModel):
    min_group_size = models.PositiveSmallIntegerField('minimum group size', default=0)

    class Meta:
        verbose_name = 'other configurations'


class Topic(models.Model):
    number = models.PositiveSmallIntegerField()
    title = models.CharField(max_length=200)

    def __str__(self):
        return '{}. {}'.format(self.number, self.title)

    class Meta:
        abstract = True


class EssayTopic(Topic):
    description = models.TextField()


class ProjectTopic(Topic):
    pass
