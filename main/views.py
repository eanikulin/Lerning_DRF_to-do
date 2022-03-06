from rest_framework.pagination import LimitOffsetPagination
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.viewsets import ModelViewSet
from .models import Project, ToDo
from .serializers import ProjectSerializer, ToDoSerializer


class ProjectLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10


class ToDoLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 20


class ProjectViewSet(ModelViewSet):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    pagination_class = ProjectLimitOffsetPagination
    # filterset_fields = ['name']

    def get_queryset(self):
        name = self.request.query_params.get('name', '')
        projects = Project.objects.all()
        if name:
            projects = projects.filter(name__contains=name)
        return projects


class ToDoViewSet(ModelViewSet):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer
    pagination_class = ToDoLimitOffsetPagination
