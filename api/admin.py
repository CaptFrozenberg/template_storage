from django.contrib import admin
from .models import TemplateField, FileTemplate

admin.site.register(FileTemplate)
admin.site.register(TemplateField)
