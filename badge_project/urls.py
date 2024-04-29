from django.contrib import admin
from django.urls import path, include
from badges.views import upload_badge  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', upload_badge, name='home'), 
    path('upload/', upload_badge, name='upload_badge'),   
]
