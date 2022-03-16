from django import forms
from django.contrib.auth import authenticate
# Models
from apps.users.models import User

from django.core.exceptions import ValidationError

class LoginForm(forms.Form):
    """ Formulario para el logeo de los usuarios """
    
    email = forms.EmailField(
        # label="E-mail"
    )
    password = forms.CharField(
        # label="Contraseña",
        widget=forms.PasswordInput
    )
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # All Widgets
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = "form-control"
            visible.field.widget.attrs['placeholder'] = f"{visible.name.title()}"
        # Widget Email
        self.fields['email'].widget.attrs['autofocus'] = True
        self.fields['email'].widget.attrs['value'] = "w10@gmail.com"
        # Widget Email
        self.fields['password'].widget.attrs['value'] = "root2020"
        
    def clean_email(self):
        email = self.cleaned_data.get('email')
        return email
        
    def clean(self):
        cleaned_data = self.cleaned_data
        if self.errors:
            return cleaned_data
        email = cleaned_data['email']
        password = cleaned_data['password']
        if not authenticate(email=email, password=password):
            raise forms.ValidationError('Usuario y/o contraseña incorrectos')
        return cleaned_data      


class UserCreateForm(forms.Form):
    """ Formulario para la creacion de usuarios """
    
    email = forms.EmailField(
        # label="E-mail"
    )
    username = forms.CharField(
        # label="E-mail"
        # min_length=6,
        help_text="Nombre usuario no debe estar en correo (min. 6)",
    )
    password1 = forms.CharField(
        # label="Contraseña",
        widget=forms.PasswordInput
    )
    password2 = forms.CharField(
        # label="Contraseña",
        widget=forms.PasswordInput
    )
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['email'].widget.attrs['autofocus'] = True
        
        self.fields['email'].widget.attrs['placeholder'] = "correo@example.com"
        self.fields['username'].widget.attrs['placeholder'] = "Nombre de usuario"
        self.fields['password1'].widget.attrs['placeholder'] = "Contraseña"
        self.fields['password2'].widget.attrs['placeholder'] = "Repetir contraseña"
        
        
    def clean_email(self):
        data = self.cleaned_data.get('email')
        if User.objects.filter(email=data).exists():
            raise forms.ValidationError("Correo ya registrado")
        return data
        
    def clean_username(self):
        data = self.cleaned_data.get('username')
        if User.objects.filter(username=data).exists():
            raise forms.ValidationError("Nombre de Usuario ya registrado")
        return data
        
    def clean_password2(self):
        if self.cleaned_data['password1'] != self.cleaned_data['password2']:
            self.add_error("password1", "Contraseñas no coinciden")
        return self.cleaned_data
    
    def save(self):    
        return User.objects.create_user(
            username=self.cleaned_data.get('username'), 
            email=self.cleaned_data.get('email'), 
            password=self.cleaned_data.get('password1'),
            first_name="Nuevo usuario"
        )