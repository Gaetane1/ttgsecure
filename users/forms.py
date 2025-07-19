from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'statut', 'photo', 'adresse', 'telephone')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'style': 'height: 35px; border-radius: 5px;'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'style': 'height: 35px; border-radius: 5px;'}),
            'statut': forms.Select(attrs={'class': 'form-select', 'style': 'height: 35px; border-radius: 5px;'}),
            'photo': forms.ClearableFileInput(attrs={'class': 'form-control', 'style': 'height: 35px; border-radius: 5px;'}),
            'adresse': forms.TextInput(attrs={'class': 'form-control', 'style': 'height: 35px; border-radius: 5px;'}),
            'telephone': forms.TextInput(attrs={'class': 'form-control', 'style': 'height: 35px; border-radius: 5px;'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Styliser password1 et password2
        self.fields['password1'].widget.attrs.update({
            'class': 'form-control',
            'style': 'height: 35px; border-radius: 5px;',
            'placeholder': 'Mot de passe'
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control',
            'style': 'height: 35px; border-radius: 5px;',
            'placeholder': 'Confirmer mot de passe'
        })

        # Placeholders pour les autres champs
        placeholders = {
            'username': 'Nom d’utilisateur',
            'email': 'Email',
            'statut': 'Statut',
            'photo': 'Photo de profil',
            'adresse': 'Adresse',
            'telephone': 'Téléphone',
        }

        for field_name, placeholder in placeholders.items():
            if field_name in self.fields:
                self.fields[field_name].widget.attrs.update({'placeholder': placeholder})



class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'statut', 'photo', 'adresse', 'telephone')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'style': 'height: 35px; border-radius: 5px;'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'style': 'height: 35px; border-radius: 5px;'}),
            'statut': forms.Select(attrs={'class': 'form-select', 'style': 'height: 35px; border-radius: 5px;'}),
            'photo': forms.ClearableFileInput(attrs={'class': 'form-control', 'style': 'height: 35px; border-radius: 5px;'}),
            'adresse': forms.TextInput(attrs={'class': 'form-control', 'style': 'height: 35px; border-radius: 5px;'}),
            'telephone': forms.TextInput(attrs={'class': 'form-control', 'style': 'height: 35px; border-radius: 5px;'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        placeholders = {
            'username': 'Nom d’utilisateur',
            'email': 'Email',
            'statut': 'Statut',
            'photo': 'Photo de profil',
            'adresse': 'Adresse',
            'telephone': 'Téléphone',
        }

        for field_name, placeholder in placeholders.items():
            if field_name in self.fields:
                self.fields[field_name].widget.attrs.update({'placeholder': placeholder})
