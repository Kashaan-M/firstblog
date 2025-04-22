from django.urls import path
from . import views
# for sitemaps
from django.contrib.sitemaps.views import sitemap
from blog.sitemaps import PostSitemap
# for RSS Feed
from .feeds import LatestPostsFeed

sitemaps = {
    "posts":PostSitemap,
}
app_name = 'blog'

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('sitemap.xml',sitemap, {"sitemaps": sitemaps}, name="sitemap"),
    path('feed/rss/',LatestPostsFeed(), name="rss_feed"),
]
