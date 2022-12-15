from django.urls import path
from . import views

urlpatterns = [
    path('show_services/', views.show_services),
]
