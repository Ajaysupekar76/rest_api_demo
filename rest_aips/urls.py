
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test_app/',include('test_app.urls')),
    path('authentication/', include('authentication.urls')),
    ]
