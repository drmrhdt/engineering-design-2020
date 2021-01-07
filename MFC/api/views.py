from rest_framework import viewsets, generics

from .serializers import UserSerializer, ServiceCategorySerializer
from core.models import User, ServiceCategory

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('last_name')
    serializer_class = UserSerializer

class ServiceCategoryViewSet(viewsets.ModelViewSet):
    queryset = ServiceCategory.objects.all().order_by('name')
    serializer_class = ServiceCategorySerializer
