
from django.contrib import admin
from django.urls import path, include
from .views import upload_picture_view, home

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", home, name="home"),
    path('api/v1/', include("api.urls")),  # Include api app URLs
    path('upload/', upload_picture_view, name='upload_picture'),
]
