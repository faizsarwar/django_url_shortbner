from rest_framework import serializers
from .models import *

class url_dataSerializer(serializers.ModelSerializer):
    class Meta:
        model= url_data
        fields = '__all__'
