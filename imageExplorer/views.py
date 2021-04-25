from rest_framework import viewsets, filters
import os
from rest_framework.response import Response

from .models import Image
from .serializer import ImageSerializer

UPLOAD_DIR = 'static/uploaded_photo/'

class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
