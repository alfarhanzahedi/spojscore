from django.contrib import admin
from django.urls import path

from core import views as core_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', core_views.index),
]

admin.site.site_header = 'Spoj Score Administration'                    
admin.site.index_title = 'Site Administration'                 
admin.site.site_title = 'Spoj Score Administration'
