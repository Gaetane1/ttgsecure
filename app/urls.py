from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('services', views.serice, name="services"),
    path('serice_infos', views.serice_info, name="serice_infos"),
    path('abouts', views.about, name="abouts"),
    path('galeries', views.galerie, name="galeries"),
    path('temoignages', views.temoignage, name="temoignages"),
    path('contacts', views.contact, name="contacts"),
    path('blogs', views.blog, name="blogs"),
    path('maisons', views.maison, name="maisons"),
    path('vehicules', views.vehucule, name="vehicules"),
    
]