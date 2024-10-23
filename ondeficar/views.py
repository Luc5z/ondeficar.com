from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView, FormView
from .models import Hotel, Lugar, Locatario, Hospede
from .forms import UserRegisterForm, HospedeForm, LocatarioForm, HotelForm, LugarForm

class HotelListView(ListView):
    model = Hotel
    template_name = 'hotel.html'

class HomeView(ListView):
    model = Lugar
    template_name = 'index.html'

class LoginView(FormView):
    form_class = AuthenticationForm
    template_name = 'login.html'
    success_url = '/'

    def form_valid(self, form):
        usuario = form.get_user()
        login(self.request, usuario)
        return super().form_valid(form)

class RegisterView(CreateView):
    form_class = UserRegisterForm
    template_name = 'register.html'
    success_url = '/login'
