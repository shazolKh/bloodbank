from django.urls import path
from . import views

urlpatterns = [
    path('settings/<username>', views.userProfile, name='profile'),
    path('profile/<user>', views.userSettings, name='settings'),
]