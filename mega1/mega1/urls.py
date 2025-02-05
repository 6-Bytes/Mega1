from django.contrib import admin
from django.urls import include,path

urlpatterns = [

    path('',include('scire.urls')),  # function_name.url
    path('admin/', admin.site.urls), 
    
]
