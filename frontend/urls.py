from django.urls import path
from frontend import views
from frontend.views import *

urlpatterns =[
    path('', HomeView.as_view(),name='home'),
    path('electronics/', ElectronicView.as_view(),name='electronics'),
    path('clothing/', ClothingView.as_view(),name='clothing'),
    path('furniture/', FurnitureView.as_view(),name='furniture'),
]