from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index, name='home'),
    path('managed/<pk>', views.Managed, name='managed'),
    path('write-blog-post', views.Write_Blog, name='write_blog'),
    # path('home1', views.HomeView.as_view(), name='home1'),
]