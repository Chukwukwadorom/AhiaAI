# from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Demographics, Retailer, Product, Sale
from .serializers import DemographicsSerializer, RetailerSerializer, ProductSerializer, SaleSerializer


class APIIndexView(APIView):
    def get(self, request):
        api_info = {
            "message": "Welcome to the AhiaAI! Here are the available endpoints:",
            "endpoints": {
                "demographics": "demographics/",
                "retailers": "retailers/",
                # Add more endpoints
            }
        }
        return Response(api_info)
    

######################## Demographic Views################################:    
class SaveDemographicsView(APIView):
    def post(self, request):
        # Deserialize the incoming JSON data
        serializer = DemographicsSerializer(data=request.data, many=True)
        
        # Validate and save the data
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Demographics data saved successfully!"}, status=status.HTTP_201_CREATED)
        return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class GetDemographicsView(APIView):
    def get(self, request, pk=None):
        if pk:  
            try:
                demographic = Demographics.objects.get(pk=pk)
            except Demographics.DoesNotExist:
                return Response({"error": "Demographic not found"}, status=status.HTTP_404_NOT_FOUND)
            serializer = DemographicsSerializer(demographic)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        
        demographics = Demographics.objects.all()
        serializer = DemographicsSerializer(demographics, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)





##########################Retailer Views#########################:
class SaveRetailerView(APIView):
    def post(self, request):
        serializer = RetailerSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Retailer data saved successfully!"}, status=status.HTTP_201_CREATED)
        return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    

class GetRetailerView(APIView):
    def get(self, request, pk=None):
        if pk:  
            try:
                retailer= Retailer.objects.get(pk=pk)
            except Retailer.DoesNotExist:
                return Response({"error": "Retailer not found"}, status=status.HTTP_404_NOT_FOUND)
            serializer = RetailerSerializer(retailer)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        
        retailer = Retailer.objects.all()
        serializer = RetailerSerializer(retailer, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    





##############################Product views##########################
class SaveProductView(APIView):
    def post(self, request):
        serializer = ProductSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Product data saved successfully!"}, status=status.HTTP_201_CREATED)
        return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    

class GetProductView(APIView):
    def get(self, request, pk=None):
        if pk:  
            try:
                product= Product.objects.get(pk=pk)
            except Product.DoesNotExist:
                return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)
            serializer =  ProductSerializer(product)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        
        product = Product.objects.all()
        serializer =  ProductSerializer(product, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    



##################Sale views#####################:
class SaveSaleView(APIView):
    def post(self, request):
        serializer = SaleSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Sale data saved successfully!"}, status=status.HTTP_201_CREATED)
        return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    

class GetSaleView(APIView):
    def get(self, request, pk=None):
        if pk:  
            try:
                sale= Sale.objects.get(pk=pk)
            except Sale.DoesNotExist:
                return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)
            serializer =  SaleSerializer(sale)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        
        sale = Sale.objects.all()
        serializer =  SaleSerializer(sale, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    