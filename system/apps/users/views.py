from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import RedirectView
from django.views.generic.edit import FormView
# Forms
from .forms import LoginForm, UserCreateForm


class LoginView(FormView):
    """ Vista para el manejo de los Login de los usuarios """
    
    template_name = "users/login.html"
    success_url = reverse_lazy("index")
    form_class = LoginForm
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(self.success_url)
        return super().dispatch(request, *args, **kwargs)
    
    def get_success_url(self):
        next_url = self.request.POST.get('next', None)
        if next_url:
            return f"{next_url}"
        else:
            return self.success_url
    
    def form_valid(self, form):
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        user = authenticate(email=email, password=password)
        login(self.request, user)
        messages.success(self.request, f"Bienvenido {user.first_name}")
        return super().form_valid(form)
    
    
class UserCreateView(FormView):
    """ Vista para el manejo de los Login de los usuarios """
    
    template_name = "users/register.html"
    success_url = reverse_lazy("index")
    form_class = UserCreateForm    
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            logout(self.request)
        return super().dispatch(request, *args, **kwargs)
    
    def form_valid(self, form):
        user = form.save()
        if user:
            login(self.request, user)
            messages.success(self.request, f"Usuario registrado correctamente {user.email}")
            return redirect(self.success_url)
        return super().form_valid(form)
    
    
class LogoutView(RedirectView):
    """ Vista para la finalizacion de las sesiones de lo usuarios """
    
    url = reverse_lazy('users:login')
    
    def get_redirect_url(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            logout(self.request)
            messages.info(self.request, f"Sesion cerrada exitosamente")
        return super().get_redirect_url(*args, **kwargs)
    