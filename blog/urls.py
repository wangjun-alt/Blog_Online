"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import xadmin
from django.contrib import admin
from django.contrib.sitemaps import views as sitemap_views
from myblog.rss import LatestPostFeed
from myblog.sitemap import PostSitemap
from myblog.views import (
    PostDetailView, IndexView, CategoryView, TagView, SearchView, AuthorView
)
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from config.views import LinkListView
from comment.views import CommentView, VerifyCaptcha
from .autocomplete import CategoryAutocomplete, TagAutocomplete

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^category/(?P<category_id>\d+)/$', CategoryView.as_view(), name='category-list'),
    url(r'^tag/(?P<tag_id>\d+)/$', TagView.as_view(), name='tag-list'),
    # url(r'^post/(?P<pk>\d+).html$', PostDetailView.as_view(), name='post-detail'),
    url(r'^post/(?P<post_id>\d+).html$', PostDetailView.as_view(), name='post-detail'),
    url(r'^search/$', SearchView.as_view(), name='search'),
    url(r'^author/(?P<owner_id>\d+)/$', AuthorView.as_view(), name='author'),
    url(r'^links/$', LinkListView.as_view(), name='links'),
    url(r'^comment/$', CommentView.as_view(), name='comment'),
    url(r'^rss|feed/', LatestPostFeed(), name='rss'),
    url(r'^sitemap\.xml$', sitemap_views.sitemap, {'sitemaps': {'posts': PostSitemap}}),
    url(r'^category-autocomplete/$', CategoryAutocomplete.as_view(), name='category-autocomplete'),
    url(r'^tag-autocomplete/$', TagAutocomplete.as_view(), name='tag-autocomplete'),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^captcha/', include('captcha.urls')),
    url(r'^verify_captcha/', VerifyCaptcha.as_view(), name='verify_captcha'),
    # url(r'^links/$', links, name='links'),
    url(r'^admin/', xadmin.site.urls, name='xadmin'),
    # url(r'^admin/', custom_site.urls, name='admin'),
    url(r'^super_admin/', admin.site.urls, name='super-admin'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
