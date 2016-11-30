# -*- encoding: utf-8 -*-
from django.contrib.sites.shortcuts import get_current_site
from rest_framework import status
from rest_framework.renderers import JSONRenderer
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import FileTemplate, TemplateField

class TemplatesView(APIView):
    renderer_classes = (JSONRenderer,)

    def get(self, request):
        domain = get_current_site(request).domain
        data = FileTemplate.objects.data(domain)
        return Response(data)