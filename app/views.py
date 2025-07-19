from django.shortcuts import render

# Create your views here.
def home(request):
    
    return render(request, "index.html")

def serice(request):
    
    return render(request, 'service.html')

def serice_info(request):
    
    return render(request, 'service_info.html')

def about(request):
    
    return render(request, 'about.html')

def galerie(request):
    
    return render(request, 'galerie.html')

def temoignage(request):
    
    return render(request, 'temoignage.html')

def contact(request):
    
    return render(request, 'contact.html')

def blog(request):
    
    return render(request, 'blog.html')

def maison(request):
    
    return render(request, 'maisons.html')

def vehucule(request):
    
    return render(request, 'vehicule.html')