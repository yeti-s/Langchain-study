from django.contrib import admin
from django.urls import path
from .views import (
    UserSignupView,
    UserLoginView, 
    UserRefreshView,
    UserDetailView, 
    UserListView
)

urlpatterns = [
    path("signup/", UserSignupView.as_view()),
    path("login/", UserLoginView.as_view()),
    path("refresh/", UserRefreshView.as_view()),
    path("detail/<int:pk>", UserDetailView.as_view()),
    path("list/", UserListView.as_view())
]
