from rest_framework.authentication import SessionAuthentication
from rest_framework.generics import RetrieveAPIView, RetrieveUpdateAPIView

from cabinet.serializers import User2Serializer


class MeAPIView(RetrieveAPIView):
    authentication_classes = (SessionAuthentication,)
    serializer_class = User2Serializer

    def get_object(self):
        return self.request.user.user2


class SetUserDataAPIView(RetrieveUpdateAPIView):
    authentication_classes = (SessionAuthentication,)
    serializer_class = User2Serializer

    def get_object(self):
        return self.request.user.user2
