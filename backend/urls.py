from django.urls import path
from .views import (SaveDemographicsView, SaveRetailerView,  APIIndexView, 
                    GetDemographicsView, GetRetailerView, SaveProductView, GetProductView, SaveSaleView
                    , GetSaleView)

urlpatterns = [
    path("",  APIIndexView.as_view(), name="index_view"),
    path('save-demographics/', SaveDemographicsView.as_view(), name='save_demographics'),
    path('demographics/', GetDemographicsView.as_view(), name='demographics_list'),
    path('demographics/<int:pk>/', GetDemographicsView.as_view(), name='demographics_detail'),

    path('save-retailers/', SaveRetailerView.as_view(), name='save_retailers'),
    path('retailers/', GetRetailerView.as_view(), name='retailer_list'),
    path('retailers/<int:pk>/', GetRetailerView.as_view(), name='retailer_detail'),

    path('save-products/', SaveProductView.as_view(), name='save_products'),
    path('products/', GetProductView.as_view(), name='products_list'),
    path('products/<int:pk>/', GetProductView.as_view(), name='products_detail'),

    path('save-sales/', SaveSaleView.as_view(), name='save_sales'),
    path('sales/', GetSaleView.as_view(), name='sales_list'),
    path('sales/<int:pk>/', GetSaleView.as_view(), name='sales_detail'),

]
