from django.urls import path
from ondeficar import views


urlpatterns = [
    path('', views.index, name='index'),
]