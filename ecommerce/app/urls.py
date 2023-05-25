from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from . import setting 

urlpatterns = [
    path('admin/',admin.site.urls)
    path('',include('app.urls'))
]+ static(setting.MEDIA_URL,document_root=setting.MEDIA_ROOT)