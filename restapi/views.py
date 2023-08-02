from rest_framework import viewsets, generics
from intaian.models import *
from .serializers import *
from rest_framework.filters import OrderingFilter, SearchFilter



class apiDataUtama(viewsets.ReadOnlyModelViewSet):
    queryset = Datautama.objects.all()
    serializer_class = DataUtamaSerializer
    filter_backends = [SearchFilter]
    search_fields = ['nipbaru']
    #filter_fields = ['company_id', 'golongan', 'jenis_kelamin']


class apiPasangan(viewsets.ReadOnlyModelViewSet):
    queryset = ModelPasangan.objects.all()
    serializer_class = pasanganSerializer
    filter_backends = [SearchFilter]
    search_fields = ['idsiasn','nama']