from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework import generics, permissions
from rest_auth.views import LoginView, LogoutView
from . import serialized
from .permissions import IsAccountOwner


class CustomLoginView(LoginView):

    permission_classes = (permissions.AllowAny,)


class CustomLogoutView(LogoutView):
    permission_classes = (permissions.IsAuthenticated,)


class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    permissions_classes = [permissions.IsAuthenticated,]
    serializer_class = serialized.UserListSerializer


class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = serialized.UserDetailSerializer
    permissions_classes = (permissions.IsAuthenticated, IsAccountOwner)


class UserRegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class =serialized.RegisterSerializer
    permission_classes = (permissions.AllowAny,)







