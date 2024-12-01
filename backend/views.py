# from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Demographics
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
    

### Demographic Views:
    
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





##Retailer Views:

class SaveRetailerView(APIView):
    def post(self, request):
        serializer = RetailerSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Retailer data saved successfully!"}, status=status.HTTP_201_CREATED)
        return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
class ProductView(APIView):
    def post(self, request):
        serializer = ProductSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Product data saved successfully!"}, status=status.HTTP_201_CREATED)
        return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
class SaleView(APIView):
    def post(self, request):
        serializer = SaleSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Sale data saved successfully!"}, status=status.HTTP_201_CREATED)
        return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)