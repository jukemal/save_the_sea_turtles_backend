from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import routers
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from app.views import DistrictViewset, SeaTurtleCountViewset

schema_view = get_schema_view(
    openapi.Info(
        title="Save the Sea Turtle API",
        default_version='v1',
        description="API for Save the Sea Turtle",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
)

router = routers.DefaultRouter()
router.register(r'districts', DistrictViewset)
router.register(r'sea_turtle_count', SeaTurtleCountViewset)

urlpatterns = [
    path('', include(router.urls)),
    url(r'^swagger(?P<format>\.json|\.yaml)$',
        schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/$', schema_view.with_ui('swagger',
                                           cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc',
                                         cache_timeout=0), name='schema-redoc'),
    path('grappelli/', include('grappelli.urls')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + \
        static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
