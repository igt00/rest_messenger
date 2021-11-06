from django.contrib.auth import login, logout
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status, views
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from auth_system.serializers import LoginSerializer, RegisterSerializer
from rest_messenger.drf_yasg import SWAGGER_NO_BODY

SWAGGER_AUTH_TAG = 'Auth system'


class LoginAPIView(views.APIView):
    authentication_classes = ()
    serializer_class = LoginSerializer
    permission_classes = (AllowAny,)

    @swagger_auto_schema(
        tags=[SWAGGER_AUTH_TAG],
        request_body=LoginSerializer(),
        responses={status.HTTP_200_OK: SWAGGER_NO_BODY},
    )
    def post(self, request):
        """Login with email and password"""
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']

        login(request, user)
        return Response(status.HTTP_200_OK)


class LogoutAPIView(views.APIView):
    @swagger_auto_schema(
        tags=[SWAGGER_AUTH_TAG],
        responses={status.HTTP_200_OK: SWAGGER_NO_BODY},
    )
    def post(self, request):
        """Logout from system"""
        logout(request)
        return Response(status.HTTP_200_OK)


class RegisterCreateAPIView(CreateAPIView):
    authentication_classes = ()
    serializer_class = RegisterSerializer
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        user = serializer.save()
        login(self.request, user)

    @swagger_auto_schema(
        tags=[SWAGGER_AUTH_TAG],
        request_body=RegisterSerializer(),
        responses={status.HTTP_201_CREATED: RegisterSerializer()},
    )
    def post(self, request, *args, **kwargs):
        """Register on system with email and password"""
        return super().post(request, *args, **kwargs)
