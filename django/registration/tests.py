from django.test import TestCase
from policy.models import Configuration, EssayTopic, ProjectTopic
from .models import Group, Application, ACCEPTED
from accounts.models import User

class ApplicationModelTests(TestCase):
    def setUp(self):
        Configuration.objects.create(min_group_size=3)

    def test_group_discount(self):
        """ Application must check the group size to determine group discount eligibility. """
        group = Group.objects.create(name='ICISTS OB')
        project_topic = ProjectTopic.objects.create(number=1, title='title')
        essay_topic = EssayTopic.objects.create(number=1, title='title', description='description')

        user1 = User.objects.create(first_name='user',
                                    last_name = '1',
                                    email='1@icists.org')
        app1 = Application.objects.create(user = user1,
                                          screening_result=ACCEPTED,
                                          group=group,
                                          topic_preference=project_topic,
                                          essay_topic=essay_topic)
        self.assertFalse(app1.group_discount())

        user2 = User.objects.create(first_name='user',
                                    last_name = '2',
                                    email='2@icists.org')
        app2 = Application.objects.create(user = user2,
                                          screening_result=ACCEPTED,
                                          group=group,
                                          topic_preference=project_topic,
                                          essay_topic=essay_topic)
        self.assertFalse(app2.group_discount())

        user3 = User.objects.create(first_name='user',
                                    last_name = '3',
                                    email='3@icists.org')
        app3 = Application.objects.create(user = user3,
                                          screening_result=ACCEPTED,
                                          group=group,
                                          topic_preference=project_topic,
                                          essay_topic=essay_topic)
        self.assertTrue(app3.group_discount())

class OrderModelTests(TestCase):
    def test_payment_status(self):
        pass

