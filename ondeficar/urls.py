from django.urls import path
from .views import HomeView, HotelListView, LoginView, RegisterView, logout_view, landing_view, HotelCreateView, LugarCreateView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('hotels/', HotelListView.as_view(), name='hotel-list'),
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', logout_view, name='logout'),
    path('landing/', landing_view, name='landing'),
    path('hotel/create/', HotelCreateView.as_view(), name='hotel_create'),
    path('lugar/create/', LugarCreateView.as_view(), name='lugar_create'),
]
