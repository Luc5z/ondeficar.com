from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView, FormView
from .models import Hotel, Lugar
from .forms import UserRegisterForm, HotelForm, LugarForm

# View para listar hotéis
class HotelListView(ListView):
    model = Hotel
    template_name = 'hotel_list.html'
    context_object_name = 'hoteis'

# View para a página inicial, listando lugares
class HomeView(ListView):
    model = Lugar
    template_name = 'index.html'
    context_object_name = 'lugares'

def mapa_view(request):
    return render(request, 'mapa.html')


def landing_view(request):
    return render(request, 'landing.html')

# View de login
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

# View para cadastro de usuários
class RegisterView(CreateView):
    form_class = UserRegisterForm
    template_name = 'register.html'
    success_url = '/login'

# View para criação de hotel
class HotelCreateView(CreateView):
    model = Hotel
    form_class = HotelForm
    template_name = 'hotel_form.html'
    success_url = '/hoteis'

# View para criação de lugar
class LugarCreateView(CreateView):
    model = Lugar
    form_class = LugarForm
    template_name = 'lugar_form.html'
    success_url = '/'

# View de logout
@login_required
def logout_view(request):
    logout(request)
    return redirect('/')
