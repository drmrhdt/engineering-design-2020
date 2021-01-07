from rest_framework import serializers

from core.models import User, ServiceCategory

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'last_name', 'first_name', 'patronyc', 'gender', 'birthday')


class ServiceCategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ServiceCategory
        fields = ('id', 'name', 'applicant_type')
