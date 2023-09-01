from rest_framework.viewsets import ModelViewSet

from apps.todo.models import Task
from .serializers import TaskSerializers


class TaskViewSet(ModelViewSet):

    # quero todos os dados que estao na tabela task
    queryset = Task.objects.all()

    serializer_class = TaskSerializers



