from rest_framework import viewsets

from reference.models import Product, VehicleType
from reference.serializers import ProductSerializer, VehicleTypeSerializer


# Create your views here.

# Company specific ViewSet to Create, Update Vehicle Types
class VehicleTypeViewSet(viewsets.ModelViewSet):
    queryset = VehicleType.objects.all()
    serializer_class = VehicleTypeSerializer
    http_method_names = ['get', 'post', 'put', 'patch']


# Company specific ViewSet to Create, Update Products
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    http_method_names = ['get', 'post', 'put', 'patch']


