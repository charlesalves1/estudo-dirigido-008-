from django.contrib import admin
from django.urls import path, include
from rest_framework.schemas import get_schema_view
from django.views.generic import TemplateView
from core.views import home
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path("", home, name="home"),
    path("admin/", admin.site.urls),
    path("api/", include("core.urls")),
    path("openapi/", SpectacularAPIView.as_view(), name="openapi-schema"),
    path("docs/", SpectacularSwaggerView.as_view(), name="swagger-ui"),

    # Swagger
    path("openapi/", get_schema_view(
        title="PATRI-TECH API",
        description="Documentação da API de inventário de bens",
        version="1.0.0"
    ), name="openapi-schema"),

    path("docs/", TemplateView.as_view(
        template_name="swagger.html"
    ), name="swagger-ui"),
]