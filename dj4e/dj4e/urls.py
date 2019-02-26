from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('home.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    # path('autos/', include('autos.urls')),
    # coment out cats during exam
    path('cats/', include('cats.urls')),
]
