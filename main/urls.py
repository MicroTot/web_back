from django.urls import path, include
from django.views.generic.base import View
from rest_framework import routers
from main.views import *
from main.serializers import User_Cat_Serializer
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from main import views


# router = routers.DefaultRouter(trailing_slash=False)
# router.register(r'user_category', UserCatViewSet.as_view())
# router.register(r'users', UserViewSet.as_view())

urlpatterns = [
    path('user_dets', AppView.as_view()),
     path('jobs', JobsViewSet.as_view()),
    path("register/", views.register, name="register"),  # <-- added
]