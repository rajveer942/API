from rest_framework import serializers
from .models import StudentModelViewSet


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentModelViewSet
        fields =['id','name','roll','city']