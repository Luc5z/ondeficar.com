from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView, FormView
from .models import Hotel, Lugar, Locatario
from .forms import UserRegisterForm, LocatarioForm, HotelForm, LugarForm

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
        # Autentica o usuário
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(self.request, username=username, password=password)
        if user is not None:
            login(self.request, user)
            return super().form_valid(form)
        else:
            return self.form_invalid(form)

class RegisterView(CreateView):
    form_class = UserRegisterForm
    template_name = 'register.html'
    success_url = '/login'

@login_required
def logout_view(request):
    logout(request)
    return redirect('/')
