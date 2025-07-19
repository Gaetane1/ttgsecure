from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('all_messages', views.message_list, name='message_list'),
    path('envoyer/', views.envoyer_message, name='envoyer_message'),
    path('decrypter/<int:message_id>/', views.decrypter_message, name='decrypter_message'),
    #path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    #path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    #path('register/', views.register_user, name='register_user'),

]
