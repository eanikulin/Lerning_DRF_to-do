from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from .models import Users
from .serializers import UsersSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import mixins


class UsersCustomViewSet(mixins.RetrieveModelMixin,
                           mixins.UpdateModelMixin,
                           mixins.ListModelMixin,
                           GenericViewSet):
   queryset = Users.objects.all()
   serializer_class = UsersSerializer
   renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
   # permission_classes = (IsAuthenticated,)
