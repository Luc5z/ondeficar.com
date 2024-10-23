from django.urls import path
from .views import HomeView, HotelListView, LoginView, RegisterView, logout_view

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('hotels/', HotelListView.as_view(), name='hotel-list'),
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', logout_view, name='logout'),
]
