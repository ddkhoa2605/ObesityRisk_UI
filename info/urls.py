from django.urls import path
from .views import info_view, visualize_data

urlpatterns = [
    path('', info_view, name='information'),  
    path('visualization/', visualize_data, name='visualization'),
]
