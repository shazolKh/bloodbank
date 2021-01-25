from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('settings/<username>', views.userProfile, name='profile'),
    path('profile/<id>', views.userSettings, name='settings'),
    path('edit_profile/<id>', views.editProfile, name='edit')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
