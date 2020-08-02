from django.contrib import admin
from django.urls import path
import main.views as views

urlpatterns = [
    path('', views.main, name='main'),
    path('get_song/', views.getSong),
    path('admin/', admin.site.urls),
]