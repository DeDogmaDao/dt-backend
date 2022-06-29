from django.urls import path
from .view import ProfileView

urlpatterns = [
    path('<str:wallet>/', ProfileView.as_view(), name='get_profile'),
    ]
