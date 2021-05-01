from rest_framework import viewsets, filters
import os
from rest_framework.response import Response

from .models import Image
from .serializer import ImageSerializer


class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
