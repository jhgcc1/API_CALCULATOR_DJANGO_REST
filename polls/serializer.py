from rest_framework import serializers
from .models import Cal

class CalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cal
        fields = ('id','var2','var1','result')