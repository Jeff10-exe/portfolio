from django.urls import path
from . import views
from .views import home, edit_profile


urlpatterns = [

 path('', views.home, name=""),

 path('register', views.register, name="register"),
 path('login', views.login, name="login"),
path('edit-profile/', edit_profile, name='edit_profile'),


]