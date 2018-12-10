from rest_framework import serializers

from .models import Project


class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        fields = (
            'id',
            'name',
            'slug',
            'logo_url',
            'summary',
            'is_published',
            'date_published',
            'url_name',
            'url',
        )
        model = Project