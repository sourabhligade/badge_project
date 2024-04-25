from django.contrib import admin
from django.urls import path, include
from badges.views import upload_badge  # Import the view function

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', upload_badge, name='home'),  # Add URL pattern for the root path
    path('upload/', upload_badge, name='upload_badge'),  # URL pattern for upload
]
