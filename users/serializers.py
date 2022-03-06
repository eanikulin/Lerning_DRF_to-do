from rest_framework import serializers
from .models import Users



class UsersSerializer(serializers.HyperlinkedModelSerializer):
    # user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    cat = serializers.StringRelatedField()
    class Meta:
        model = Users
        fields = "__all__"
