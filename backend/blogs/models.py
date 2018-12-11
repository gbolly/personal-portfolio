from django.db import models
from markdownx.models import MarkdownxField


class BlogManager(models.Manager):
    def get_queryset(self):
        return super(BlogManager, self).get_queryset().filter(is_published=True)


class Blog(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    cover_image_url = models.URLField(blank=True)
    summary = models.TextField(max_length=255, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    text = MarkdownxField()
    is_published = models.BooleanField(default=False)
    date_published = models.DateTimeField(blank=True)

    objects = models.Manager()
    visible = BlogManager()

    def __str__(self):
        return self.title if self.is_published else "[DRAFT] " + self.title

    class Meta:
        ordering = ['-is_published', '-date_published', '-date_created', ]