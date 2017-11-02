from django.db import models
from django.core.exceptions import ObjectDoesNotExist
from django.utils.deconstruct import deconstructible
from djmoney.models.fields import MoneyField
from djmoney.money import Money

from accounts.models import User
from ams2.settings import CURRENCY_CHOICES
from policy.models import AccommodationOption, EssayTopic, ProjectTopic, Configuration, Price

EARLY, REGULAR, LATE = 'E', 'R', 'L'
APP_STAGES = [
    (EARLY, 'Early'),
    (REGULAR, 'Regular'),
    (LATE, 'Late'),
]

ACCEPTED, REJECTED, PENDING = 'A', 'R', 'P'
SCREENING_RESULTS = [
    (ACCEPTED, 'Accepted'),
    (REJECTED, 'Rejected'),
    (PENDING, 'Pending'),
]


class Group(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

    def size(self):
        return self.applications.count()

    class Meta:
        verbose_name = 'applicant group'


class Application(models.Model):
    user = models.ForeignKey(User, related_name='applications')
    stage = models.CharField(max_length=1, choices=APP_STAGES)
    screening_result = models.CharField(max_length=1, choices=SCREENING_RESULTS, default=PENDING)
    disclose_result = models.BooleanField(default=False)

    topic_preference = models.ForeignKey(ProjectTopic, related_name='applications')
    essay_topic = models.ForeignKey(EssayTopic, related_name='applications')
    essay_text = models.TextField(blank=True)

    group = models.ForeignKey(Group, related_name='applications', blank=True, null=True)
    visa_letter = models.BooleanField(default=False)
    financial_aid = models.BooleanField(default=False)
    previous_participation = models.BooleanField(default=False)

    last_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} ({})'.format(self.user.get_full_name(), self.stage)

    def group_discount(self):
        min_group_size = Configuration.objects.get().min_group_size
        accepted_peers = self.group.applications.filter(screening_result=ACCEPTED)
        return accepted_peers.count() >= min_group_size


class Order(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    preferred_currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, default='KRW')
    paid_amount = MoneyField(max_digits=7, decimal_places=0, default=0, default_currency='KRW')

    accommodation = models.ForeignKey(AccommodationOption, related_name='orders')
    dietary_preferences = models.CharField(max_length=100, blank=True, null=True)
    options = models.ManyToManyField(Price, related_name='orders', blank=True)

    def __str__(self):
        return self.user.get_full_name()

    def total_cost(self):
        cost = Money(0, self.preferred_currency)

        if self.preferred_currency == 'KRW':
            cost.amount += sum([option.price_krw.amount for option in self.options.all()])
        elif self.preferred_currency == 'USD':
            cost.amount += sum([option.price_usd.amount for option in self.options.all()])

        return cost

    def option_checker(self, code):
        try:
            return self.options.get(code=code) is not None
        except ObjectDoesNotExist:
            return False

    def breakfast_option(self):
        return self.option_checker('breakfast')
    breakfast_option.boolean = True

    def pre_option(self):
        return self.option_checker('pre')
    pre_option.boolean = True

    def post_option(self):
        return self.option_checker('post')
    post_option.boolean = True

    def payment_status(self):
        unpaid_amount = self.total_cost().amount - self.paid_amount.amount
        if unpaid_amount == 0:
            return 'Clear'
        elif unpaid_amount > 0:
            unpaid = Money(unpaid_amount, self.preferred_currency)
            return 'Paid less ({})'.format(str(unpaid))
        else:
            overpaid = Money(-unpaid_amount, self.preferred_currency)
            return 'Paid more ({})'.format(str(overpaid))
