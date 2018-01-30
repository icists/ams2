from django.shortcuts import get_object_or_404
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import Application, Order
from .serializers import SimpleApplicationSerializer, ApplicationSerializer, SimpleOrderSerializer, OrderSerializer


class ApplicationList(ListCreateAPIView):
    serializer_class = SimpleApplicationSerializer

    def get_queryset(self):
        return Application.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ApplicationDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = ApplicationSerializer
    lookup_field = 'id'

    def get_queryset(self):
        return Application.objects.filter(user=self.request.user)


class OrderList(ListCreateAPIView):
    serializer_class = SimpleOrderSerializer

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class OrderDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = OrderSerializer

    def get_object(self):
        return get_object_or_404(Order, user=self.request.user)
