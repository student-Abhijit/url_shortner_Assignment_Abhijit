from django.contrib import admin
from django.urls import path, include
from shortener.views import redirect_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('shortener.urls')),
    path('<str:short_code>/', redirect_view, name='redirect'),
]
