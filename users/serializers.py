from rest_framework import serializers
from rest_framework.serializers import HyperlinkedModelSerializer
from .models import Users



class UsersSerializer(serializers.ModelSerializer):
# class UsersSerializer(HyperlinkedModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Users
        fields = "__all__"
