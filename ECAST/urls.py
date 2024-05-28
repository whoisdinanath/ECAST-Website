
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/committee/', include('committee.urls')),
    path('api/event/', include('event.urls')),
    path('api/project/', include('projects.urls')),
    path('api/intake/', include('intake.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
