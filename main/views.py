from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from rest_framework import viewsets, permissions
from rest_framework import generics
from django.contrib.auth import login, authenticate

# Custom imports
from main.models import Jobs, User_Category
from main.permissions import ReadOnly
from main.forms import RegisterForm
from main.serializers import Jobs_Serializer, User_Cat_Serializer, UserSerializer

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (ReadOnly, )


class UserCatViewSet(viewsets.ModelViewSet):
    queryset = User_Category.objects.all()
    serializer_class = User_Cat_Serializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class AppView(generics.ListCreateAPIView):
    serializer_class = User_Cat_Serializer

    def get_queryset(self):
        user = self.request.user
        return User_Category.objects.filter(user=user)


class JobsViewSet(generics.ListCreateAPIView):
    queryset = Jobs.objects.all()
    serializer_class = Jobs_Serializer



def register(response):
    if response.method == 'POST':
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(response, user)
            return redirect('http://localhost:8000')

        return redirect("http://localhost:8000/register/")

    else:
        form = RegisterForm()
    return render(response, "registration/registration.html", {"form":form})