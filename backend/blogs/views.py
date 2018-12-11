from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import viewsets, permissions
from . import models, serializers


class BlogViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = models.Blog.objects.all()
    serializer_class = serializers.BlogSerializer

    def get_queryset(self):
        if self.request.auth:
            return models.Blog.objects.all()
        else:
            return models.Blog.visible.all()

    def retrieve(self, request, pk=None):
        queryset = self.queryset

        try:  # retrieve blog by primary key
            pk = int(pk)
            blog = get_object_or_404(self.get_queryset(), pk=pk)
            serializer = self.get_serializer(blog)
            return Response(serializer.data)

        except:  # retrieve blog by slug
            blog = get_object_or_404(self.get_queryset().filter(slug=pk))
            serializer = self.get_serializer(blog)
            return Response(serializer.data)