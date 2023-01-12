from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name ='home'),
    path('profile', views.profile, name = 'profile'),
    path("game", views.game, name = 'game'),
    path("register", views.register_request, name="register"),
    path("login", views.login_request, name="login"),
    path('game/dragons_tail', views.play, name ='play_game')
]