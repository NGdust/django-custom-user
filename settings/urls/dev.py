from django.conf import settings
from django.views.generic import TemplateView
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from .base import *

schema_view = get_schema_view(
    openapi.Info(
        title="App",
        default_version='v1',
    ),
    url=settings.SWAGGER_BASE_URL
)

dev_urlpatterns = [
    path('api/swagger/', TemplateView.as_view(
        template_name='swagger-ui.html',
        extra_context={'schema_url': 'openapi-schema'}
    ), name='swagger'),
    path('api/openapi/', schema_view.with_ui('swagger', cache_timeout=0), name='openapi-schema'),
]

urlpatterns += dev_urlpatterns