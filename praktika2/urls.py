from django.contrib import admin
from django.urls import path, include
from .router import router
from a_s import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('', include('a_s.urls')),
]

