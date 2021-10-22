from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import game_detail

urlpatterns = [
    path('detail/(?P<id>\d+)/$',
         game_detail,
         name="gameplay_detail"),
    path ('make_move/(?P<id>\d+)/$',
          make_move,
          name="gameplay_make_move"),
]