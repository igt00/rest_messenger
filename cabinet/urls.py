from django.urls import path

from cabinet.views import MeAPIView, SetUserDataAPIView

urlpatterns = [
    path('me/', MeAPIView.as_view(), name='me'),
    path('set_data/', SetUserDataAPIView.as_view(), name='set_user2_data'),
]
