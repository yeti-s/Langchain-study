from django.urls import path
from .views import (
    AccountListView,
    AccountSignupView,
    AccountDetailView,
    transfer
)

urlpatterns = [
    path("list/", AccountListView.as_view()),
    path("signup/", AccountSignupView.as_view()),
    path("detail/<int:pk>", AccountDetailView.as_view()),
    path("transfer/", transfer)
]
