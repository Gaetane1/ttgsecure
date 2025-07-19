from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('manage/user', include('users.urls')),         # Les routes d'authentification seront directement accessibles
    path('message/', include('messaging.urls')),     # La messagerie à la racine aussi
    path('', include('app.urls')),     # La application à la racine aussi
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
