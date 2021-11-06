from auth_system.views import LoginAPIView, LogoutAPIView, RegisterCreateAPIView
from django.urls import path

urlpatterns = [
    path('login/', LoginAPIView.as_view(), name='login'),
    path('logout/', LogoutAPIView.as_view(), name='logout'),
    path('register/', RegisterCreateAPIView.as_view(), name='register'),
]
