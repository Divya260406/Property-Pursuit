from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from adminapp import views as admin_views  # importing the common dashboard

urlpatterns = [
    path('', admin_views.dashboard, name='dashboard'),
    path('adminapp/', include('adminapp.urls')),
    path('buyerapp/', include('buyerapp.urls')),
    path('dealerapp/', include('dealerapp.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
