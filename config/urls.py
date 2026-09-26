from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView
from django.contrib.sitemaps.views import sitemap
from website.sitemaps import StaticViewSitemap

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('website.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': {'static': StaticViewSitemap}}, name='django.contrib.sitemaps.views.sitemap'),
]
