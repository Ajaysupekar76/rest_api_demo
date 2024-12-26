
from django.urls import path
#from .views import CompanyView
from .views import RegisterUserAPIView,LoginView,DashboardView

urlpatterns = [
    #path('companies/', CompanyView.as_view(), name='companies'),
    path('register/', RegisterUserAPIView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),


]
