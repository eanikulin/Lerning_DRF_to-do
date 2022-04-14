from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from .models import Users
from .serializers import UsersSerializer, UsersDetailSerializer
from rest_framework.permissions import IsAuthenticated
# from rest_framework import mixins
# from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework import generics


# class UsersCustomViewSet(mixins.RetrieveModelMixin,
#                          mixins.UpdateModelMixin,
#                          mixins.ListModelMixin,
#                          GenericViewSet):
class UsersCustomViewSet(generics.ListAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    permission_classes = (IsAuthenticated,)

    def get_serializer_class(self):
        if self.request.version == '2':
            return UsersDetailSerializer
        return UsersSerializer

