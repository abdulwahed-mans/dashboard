from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView


urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('accounts/', include('accounts.urls')),
    path('profiles/', include('profiles.urls')),
    path('pages/', include('pages.urls')),
    path('admin/', admin.site.urls),
]