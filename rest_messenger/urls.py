"""rest_messenger URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""  # noqa:D400,RST203,RST301,RST201
from django.contrib import admin
from django.urls import include, path

from rest_messenger.drf_yasg import schema_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('auth_system.urls'), name='auth_system'),
    path('api/cabinet/', include('cabinet.urls'), name='api_cabinet'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
