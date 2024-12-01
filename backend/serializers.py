from rest_framework import serializers
from backend.models import Demographics, Retailer, Product, Sale

class DemographicsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Demographics
        fields = '__all__'

class RetailerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Retailer
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields = '__all__'