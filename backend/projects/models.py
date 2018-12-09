from django.db import models


# Create your models here.
class ProjectManager(models.Manager):
    def get_queryset(self):
        return super(ProjectManager, self).get_queryset().filter(is_published=True)


class Project(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    logo_url = models.URLField(blank=True)
    summary = models.TextField(max_length=255, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    url_name = models.CharField(max_length=50, default='Website')
    url = models.URLField()
    is_published = models.BooleanField(default=False)
    date_published = models.DateField(blank=True)

    objects = models.Manager()
    visible = ProjectManager()

    def __str__(self):
        return self.name if self.is_published else "[DRAFT] " + self.name

    class Meta:
        ordering = ['-is_published', '-date_published', '-date_created', ]