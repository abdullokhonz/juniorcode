from django.urls import path
from . import views
from django.contrib.sitemaps.views import sitemap
from .sitemaps import StaticViewSitemap, CourseSitemap, StudentSitemap, TeacherSitemap

sitemaps = {
    'static': StaticViewSitemap,
    'courses': CourseSitemap,
    'students': StudentSitemap,
    'teachers': TeacherSitemap,
}


urlpatterns = [
    path('', views.main, name='main'),
    path('robots.txt', views.robots_txt, name='robots_txt'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='sitemap'),
    # path('sitemap.xml', views.sitemap, name='sitemap'),
]
