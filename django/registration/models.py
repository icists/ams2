from django.db import models
from djmoney.models.fields import MoneyField

from accounts.models import User
from ams2.settings import CURRENCY_CHOICES
from policy.models import AccommodationOption, EssayTopic, ProjectTopic, Configuration

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
        return self.group.applications.count() >= min_group_size


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

    def total(self):
        price = 0
        application = Application.objects.get(user=self.user, screening_result=ACCEPTED)
        # TODO
        return price

    def payment_status(self):
        pass
