from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from messaging.forms import CustomUserCreationForm
from .models import Message
from .utils import text_to_binary, binary_to_text


def message_list(request):
    messages = Message.objects.all().order_by('-date_envoye')
    return render(request, 'messaging.html', {'messages': messages})


@login_required
def envoyer_message(request):
    if request.method == 'POST':
        texte = request.POST.get('texte')
        binaire = text_to_binary(texte)
        Message.objects.create(auteur=request.user, binaire=binaire)
        return redirect('message_list')
    return render(request, 'message_form.html')

@login_required
def decrypter_message(request, message_id):
    message = get_object_or_404(Message, id=message_id)
    texte = binary_to_text(message.binaire)
    return render(request, 'decrypt_message.html', {'texte': texte, 'binaire': message.binaire})

"""
@login_required
def register_user(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # 🔑 Connexion auto
            return redirect('message_list')  # 🔁 Redirection
    else:
        form = CustomUserCreationForm()

    return render(request, 'register.html', {'form': form})"""