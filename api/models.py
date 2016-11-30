# -*- encoding: utf-8 -*-
from django.db import models

class FileTemplateManager(models.Manager):

    def data(self, domain):
        data = []
        templates = self.all()        
        for template in templates:
            doc = getattr(template, 'doc', None)
            doc_url = None
            if doc:
                doc_url = ''.join(['http://', domain, template.doc.url])

            dll = getattr(template, 'dll', None)
            dll_url = None
            if dll:
                dll_url = ''.join(['http://', domain, template.dll.url])

            data_rec = {
                'name': template.name,
                'doc': doc_url,
                'dll': dll_url,
                'fields': [item.field_key
                           for item in TemplateField.objects.filter(template=template)]
            }
            data.append(data_rec)
        return data


class FileTemplate(models.Model):

    name = models.CharField(max_length=150, verbose_name='Название')
    param = models.SlugField(max_length=50, unique=True, verbose_name='Псевдоним')
    doc = models.FileField(null=True, blank=True, verbose_name='Документ .docx')
    dll = models.FileField(null=True, blank=True, verbose_name='Шаблонизатор .dll')

    objects = FileTemplateManager()

    def __str__(self):
        return self.name


class TemplateField(models.Model):
    template = models.ForeignKey(FileTemplate, to_field='param', verbose_name='Шаблон')
    field_key = models.SlugField(max_length=50, verbose_name='Ключ поля')

    class Meta:
        unique_together = (("template", "field_key"),)

    def __str__(self):
        return 'template: {} field: {}'.format(self.template, self.field_key)
