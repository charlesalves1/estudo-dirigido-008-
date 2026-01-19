from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path("", RedirectView.as_view(url='/docs/', permanent=True)), # Redireciona a raiz para o Swagger UI
    path("admin/", admin.site.urls),
    path("api/", include("core.urls")),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"), # View do esquema OpenAPI
    path("docs/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"), # Interface do Swagger UI
]