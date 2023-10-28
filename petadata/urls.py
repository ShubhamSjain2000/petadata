"""
URL configuration for petadata project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
"""
from django.urls import re_path
from rest_framework import permissions
from django.contrib import admin
from django.urls import path, include

from drf_yasg2.views import get_schema_view
from drf_yasg2 import openapi
from django.views import View

schema_view = get_schema_view(
    openapi.Info(
        title="PetaData API",
        default_version='v1',
        description="Test description",
        contact=openapi.Contact(email="codetestbyshubham@gmail.com"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path("admin/", admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path("auth_management/", include('auth_management.urls')),
    path('workflow/', include('workflow.urls'))
]
