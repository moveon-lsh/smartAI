from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
# from posts.urls import first
urlpatterns = [
    path('posts/', include('posts.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
