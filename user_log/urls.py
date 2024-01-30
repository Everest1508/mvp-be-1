# yourapp/urls.py

from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenVerifyView

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/',LoginView.as_view(),name = 'login'),
    path('users/',Users.as_view(),name = 'users'),
    path('colleges/', CollegeListCreateView.as_view(), name='college-list-create'),
    path('games/', GamesListCreateView.as_view(), name='games-list-create'),
    path("verify/", VerifyOTPView.as_view(), name=""),
    
    # events
    
    path('subevent/',SubEventCreateAPIView.as_view(),name=""),
    path('participate/<int:id>/',AddUserToEventView.as_view(),name=""),
    path('event/',MainEventCreateAPIView.as_view(),name=""),
    path('withdraw/<int:id>/',WithdrawUserFromEventView.as_view(),name=""),
    path('myevent/',MyEventView.as_view(),name=""),
    path('mainevent/<int:id>/',AddSubEventView.as_view(),name=""),
]
