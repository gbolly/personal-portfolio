from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import viewsets, permissions
from . import models, serializers


class ProjectViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = models.Project.objects.all()
    serializer_class = serializers.ProjectSerializer

    def get_queryset(self):
        if self.request.auth:
            return models.Project.objects.all()
        else:
            return models.Project.visible.all()

    def retrieve(self, request, pk=None):
        queryset = self.queryset

        try:  # retrieve project by primary key
            pk = int(pk)
            project = get_object_or_404(self.get_queryset(), pk=pk)
            serializer = self.get_serializer(project)
            return Response(serializer.data)

        except:  # retrieve project by slug
            project = get_object_or_404(self.get_queryset().filter(slug=pk))
            serializer = self.get_serializer(project)
            return Response(serializer.data)