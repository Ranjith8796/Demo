from django.contrib import admin
from django.urls import path
from secondapp import views as v2

urlpatterns = [
   
    path('admin/', admin.site.urls),
    path('time/',v2.tellmetime),
   
]