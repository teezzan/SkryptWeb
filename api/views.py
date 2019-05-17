from rest_framework import viewsets

from .models import Skrypt, Data
from .serializer import SkryptSerializer, DataSerializer


class SkryptViewSet(viewsets.ModelViewSet):
    """
    A ViewSet for viewing, detailing and editing Skrypt.
    """

    queryset = Skrypt.objects.all()
    serializer_class = SkryptSerializer


class DataViewSet(viewsets.ModelViewSet):
    """
    A ViewSet for viewing, detailing and editing Data.
    """

    queryset = Data.objects.all()
    serializer_class = DataSerializer
