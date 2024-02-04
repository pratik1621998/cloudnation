from rest_framework import serializers
from app.models import *

class UserAppSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserAppDetails
        fields = "__all__"

class EnvironmentVariableSerializer(serializers.ModelSerializer):

    class Meta:
        model = EnvironmentVariable
        fields = "__all__"





        


