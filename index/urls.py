from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index, name='home'),
    # path('<username>/new_post', views.posts, name='new_post'),
    # path('home1', views.HomeView.as_view(), name='home1'),
]