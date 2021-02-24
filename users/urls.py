from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('settings/<username>', views.userProfile, name='profile'),
    path('profile/<str:pk>', views.userSettings, name='settings'),
    path('edit_profile/<str:pk>', views.editProfile, name='edit')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# shazol_kh 123password987
# shazol_1 123password987
