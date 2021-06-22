from django.contrib import admin
from django.urls import path
from firstapp import views as v1

urlpatterns = [
   
    path('admin/', admin.site.urls),
    path('home/',v1.home),
    path('gm/',v1.gm_),
    path('ga/',v1.ga_),
    path('gn/',v1.gn_),
        
]