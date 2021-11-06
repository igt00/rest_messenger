from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.authentication import SessionAuthentication
from rest_framework.generics import RetrieveAPIView, RetrieveUpdateAPIView

from cabinet.serializers import User2Serializer

CABINET_SWAGGER_TAG = 'API cabinet'


class MeAPIView(RetrieveAPIView):
    authentication_classes = (SessionAuthentication,)
    serializer_class = User2Serializer

    def get_object(self):
        return self.request.user.user2

    @swagger_auto_schema(tags=[CABINET_SWAGGER_TAG], responses={status.HTTP_200_OK: serializer_class()})
    def get(self, request, *args, **kwargs):
        """Get main information for user"""
        return super().get(request, *args, **kwargs)


class SetUserDataAPIView(RetrieveUpdateAPIView):
    authentication_classes = (SessionAuthentication,)
    serializer_class = User2Serializer

    def get_object(self):
        return self.request.user.user2

    @swagger_auto_schema(tags=[CABINET_SWAGGER_TAG], responses={status.HTTP_200_OK: serializer_class()})
    def get(self, request, *args, **kwargs):
        """Get personal data for user"""
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        tags=[CABINET_SWAGGER_TAG],
        request_body=serializer_class(),
        responses={status.HTTP_200_OK: serializer_class()},
    )
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)
