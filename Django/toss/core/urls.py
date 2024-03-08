from django.contrib import admin
from django.urls import path
from .views import UserList, UserDetail

urlpatterns = [
    path("user_list/", UserList.as_view()),
    path("user/<int:pk>", UserDetail.as_view())
]
