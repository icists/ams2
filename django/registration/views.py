from django.shortcuts import get_object_or_404
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import Application, Order
from .serializers import ApplicationSerializer, OrderSerializer
import logging
logger = logging.getLogger(__name__)


class ApplicationList(ListCreateAPIView):
    serializer_class = ApplicationSerializer

    def get_queryset(self):
        return Application.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # logger.warning("* * * * * * * * * * * {}".format(self.request.group))
        serializer.save(user=self.request.user)


class ApplicationDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = ApplicationSerializer
    lookup_field = 'id'

    def get_queryset(self):
        return Application.objects.filter(user=self.request.user)

    def perform_update(self, serializer):
        # logger.warning("* * * * * * * * * * * {}".format(self.request.group))
        instance = serializer.save()
        # send_email_confirmation(user=self.request.user, modified=instance)


class OrderList(ListCreateAPIView):
    serializer_class = OrderSerializer

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class OrderDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = OrderSerializer

    def get_object(self):
        return get_object_or_404(Order, user=self.request.user)
