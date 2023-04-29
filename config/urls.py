from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from rest_framework.routers import DefaultRouter
from django.conf.urls.static import static
from main.views import *

from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
   openapi.Info(
      title="AUDIO API",
      default_version='v1',
      description="O'quv maqsadlarida foydalanish uchun",
      contact=openapi.Contact(email="<frjavohir@gmail.com>"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

router=DefaultRouter()
router.register('audios',AudioViewSet)
router.register('topics',TopicViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('docs/',schema_view.with_ui('swagger',cache_timeout=0)),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
