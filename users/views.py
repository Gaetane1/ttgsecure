from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .forms import CustomUserCreationForm
from django.contrib.admin.views.decorators import staff_member_required
# Create your views here.

@staff_member_required
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Connecte automatiquement l’utilisateur après inscription
            return redirect('message_list')  # Ou une autre URL de ton choix
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')