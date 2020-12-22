from rest_framework import serializers

from django.db import models

from django.contrib.auth.models import User
from .models import Query, Human


class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Human
        fields = '__all__'