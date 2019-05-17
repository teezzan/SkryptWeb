from rest_framework import serializers
from .models import Skrypt, Data


class SkryptSerializer(serializers.ModelSerializer):
	class Meta:
		model = Skrypt
		fields = '__all__'

class DataSerializer(serializers.ModelSerializer):
	class Meta:
		model = Data
		fields = '__all__'