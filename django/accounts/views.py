from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView

from .models import School
from .serializers import SchoolSerializer, UserSerializer


class SchoolList(ListAPIView):
    serializer_class = SchoolSerializer

    def get_queryset(self):
        queryset = School.objects.all()
        query = self.request.query_params.get('query', None)
        if query is not None:
            queryset = queryset.filter(name__icontains=query)
        return queryset.order_by('name')


class UserView(RetrieveUpdateAPIView):
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user
