from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from drf_spectacular.views import (SpectacularAPIView, SpectacularSwaggerView, )
from django.conf.urls.static import static
from django.conf import settings

from i_table.views import ITableViewSet

from other_info.views import UserInfoViewSet, NewsViewSet

table_router = DefaultRouter()
user_router = DefaultRouter()
news_router = DefaultRouter()
table_router.register('infotable', ITableViewSet)
user_router.register('user', UserInfoViewSet)
news_router.register('news', NewsViewSet)

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
                  path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
                  path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
                  path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
              ] + table_router.urls + user_router.urls + news_router.urls  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
