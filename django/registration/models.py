from django.db import models
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

    breakfast_option = models.BooleanField(default=False)
    pre_option = models.BooleanField('pre-conference banquet', default=False)
    post_option = models.BooleanField('post-conference tour', default=False)

    def __str__(self):
        return self.user.get_full_name()

    def total_cost(self):
        cost = Money(0, self.preferred_currency)
        prices = {}
        price_objects = Price.objects.all()
        for obj in price_objects:
            if self.preferred_currency == 'KRW':
                prices[obj.code] = obj.price_krw.amount
            elif self.preferred_currency == 'USD':
                prices[obj.code] = obj.price_usd.amount

        try:
            application = Application.objects.get(user=self.user, screening_result=ACCEPTED)
        except Application.DoesNotExist:
            application = None

        if application is None:
            pass
        elif application.stage == EARLY:
            cost.amount += prices.get('early', 0)
        elif application.stage == REGULAR:
            cost.amount += prices.get('regular', 0)
        elif application.stage == LATE:
            cost.amount += prices.get('late', 0)

        if self.breakfast_option:
            cost.amount += prices.get('breakfast', 0)
        if self.pre_option:
            cost.amount += prices.get('pre', 0)
        if self.post_option:
            cost.amount += prices.get('post', 0)

        return cost

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
