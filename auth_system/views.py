from django.contrib.auth import login, logout
from rest_framework import views, status
from rest_framework.authentication import SessionAuthentication
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from auth_system.models import User2
from auth_system.serializers import LoginSerializer, RegisterSerializer


class LoginAPIView(views.APIView):
    authentication_classes = ()
    serializer_class = LoginSerializer
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']

        login(request, user)
        return Response(status.HTTP_200_OK)


class LogoutAPIView(views.APIView):
    authentication_classes = (SessionAuthentication,)

    def post(self, request):
        logout(request)
        return Response(status.HTTP_200_OK)


class RegisterCreateAPIView(CreateAPIView):
    authentication_classes = ()
    serializer_class = RegisterSerializer
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        user = serializer.save()
        User2.objects.create(user=user)
        login(self.request, user)
