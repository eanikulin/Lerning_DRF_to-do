from rest_framework.viewsets import ModelViewSet
from .models import Users
from .serializers import UsersSerializer
from rest_framework.permissions import IsAuthenticated

class UsersModelViewSet(ModelViewSet):
   queryset = Users.objects.all()
   serializer_class = UsersSerializer
   permission_classes = (IsAuthenticated,)
