from rest_framework.generics import ListAPIView, RetrieveAPIView

from .models import Stage, PaymentInfo, Price, AccommodationOption, EssayTopic, ProjectTopic
from .serializers import \
    StageSerializer,\
    PaymentInfoSerializer,\
    PriceSerializer,\
    AccommodationOptionSerializer,\
    EssayTopicSerializer,\
    ProjectTopicSerializer


class StageView(RetrieveAPIView):
    serializer_class = StageSerializer

    def get_object(self):
        return Stage.objects.get()


class PaymentInfoView(RetrieveAPIView):
    serializer_class = PaymentInfoSerializer

    def get_object(self):
        return PaymentInfo.objects.get()


class OptionList(ListAPIView):
    serializer_class = PriceSerializer
    queryset = Price.objects.all()


class AccommodationOptionList(ListAPIView):
    serializer_class = AccommodationOptionSerializer
    queryset = AccommodationOption.objects.all()


class EssayTopicList(ListAPIView):
    serializer_class = EssayTopicSerializer
    queryset = EssayTopic.objects.all()


class ProjectTopicList(ListAPIView):
    serializer_class = ProjectTopicSerializer
    queryset = ProjectTopic.objects.all()
