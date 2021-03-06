from rest_framework import serializers
from .models import Singer,Song


# class SingerSerializer(serializers.ModelSerializer):
#     rajveer=S
#     class Meta:
#         model=Singer
#         fields='__all__'
class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model=Song
        fields='__all__'
class SingerSerializer(serializers.ModelSerializer):
    rajveer=SongSerializer(many=True,read_only=True)
    class Meta:
        model=Singer
        fields='__all__'