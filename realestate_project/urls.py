
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('properties/', include('properties.urls')),
    path('', RedirectView.as_view(url='properties/')),
    path('google-site-verification: google74e714dd7d7dd743.html' , serve ,{
        'document_root' : settings.STATIC_ROOT,
        'path' : 'google_verification/google-site-verification: google74e714dd7d7dd743.html',
        }),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)