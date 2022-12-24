from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app01.urls')),
    # path('social-auth/', include('social_django.urls', namespace="social")),
] 

urlpatterns += static(settings.STATIC_URL, document__root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document__root=settings.MEDIA_ROOT)
