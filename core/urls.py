from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('ondeficar.urls')),
    path('admin/', admin.site.urls),
    path('', include('ondeficar.urls')),
]
