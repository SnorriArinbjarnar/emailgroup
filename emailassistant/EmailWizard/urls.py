

from django.urls import path, include 
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('<int:pk>/', views.GroupDetailView.as_view(), name='group_detail')
]
