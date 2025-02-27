"""
URL configuration for rest_aips project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
#from .views import CompanyView
from .views import RegisterUserAPIView,LoginAPIView,ValidateTokenAPIView

urlpatterns = [
    #path('companies/', CompanyView.as_view(), name='companies'),
    path('register/', RegisterUserAPIView.as_view(), name='register'),
    path('login/', LoginAPIView.as_view(), name='login'),

    path('validate-token/', ValidateTokenAPIView.as_view(), name='validate-token'),

]
