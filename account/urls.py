from django.urls import path
from . import views

urlpatterns = [
    path('', views.UserListView.as_view()), #accounts/
    path('<int:pk>/', views.UserDetailView.as_view()), #account/<id>/
    path('login/', views.CustomLoginView.as_view()), #account/login/
    path('logout/', views.CustomLogoutView.as_view()), #account/logout/
    path('register/', views.UserRegisterView.as_view())
]