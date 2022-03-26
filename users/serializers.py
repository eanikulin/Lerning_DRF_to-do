from rest_framework import serializers
from .models import Users



class UsersSerializer(serializers.HyperlinkedModelSerializer):
    # user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    cat = serializers.StringRelatedField()
    user_permissions = serializers.StringRelatedField()
    groups = serializers.StringRelatedField()
    # group-detail = serializers.StringRelatedField()
    class Meta:
        model = Users
        exclude = ['password']
