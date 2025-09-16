from rest_framework.serializers import ModelSerializer
from .models import Product

# Create your views here


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = [
            "name",
            "description",
            "price",
            "available",
            "photo",
        ]
