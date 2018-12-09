from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin
from .models import Project


admin.site.register(Project)