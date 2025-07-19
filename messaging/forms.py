from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        label="Adresse e-mail",
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'style': 'padding: 12px; font-size: 1em; width: 100%;'
        })
    )

    username = forms.CharField(
        label="Nom d’utilisateur",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'style': 'padding: 12px; font-size: 1em; width: 100%;'
        })
    )

    password1 = forms.CharField(
        label="Mot de passe",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'style': 'padding: 12px; font-size: 1em; width: 100%;'
        })
    )

    password2 = forms.CharField(
        label="Confirmez le mot de passe",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'style': 'padding: 12px; font-size: 1em; width: 100%;'
        })
    )

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def clean_password1(self):
        password = self.cleaned_data.get("password1")
        if len(password) < 10:
            raise forms.ValidationError("Le mot de passe doit contenir au moins 10 caractères.")
        return password
