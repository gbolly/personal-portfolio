from rest_framework import serializers
import markdown2
from .models import Blog


class BlogSerializer(serializers.ModelSerializer):
    html_text = serializers.SerializerMethodField()

    class Meta:
        model = Blog
        fields = (
            'id',
            'title',
            'slug',
            'cover_image_url',
            'summary',
            'text',
            'html_text',
            'is_published',
            'date_published',
        )

    def get_html_text(self, blog):
        return markdown2.markdown(blog.text, extras=['target-blank-links', 'fenced-code-blocks', ])