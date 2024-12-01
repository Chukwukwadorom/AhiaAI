from django.urls import path
from .views import SaveDemographicsView, SaveRetailerView,  APIIndexView, GetDemographicsView

urlpatterns = [
    path("",  APIIndexView.as_view(), name="index_view"),
    path('save-demographics/', SaveDemographicsView.as_view(), name='save_demographics'),
    path('save-retailers/', SaveRetailerView.as_view(), name='save_retailers'),
    path('demographics/', GetDemographicsView.as_view(), name='demographics_list'),
    path('demographics/<int:pk>/', GetDemographicsView.as_view(), name='demographics_retrieve'),
]
