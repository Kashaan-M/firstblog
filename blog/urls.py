from django.urls import path
from . import views

# for RSS Feed
from .feeds import LatestPostsFeed

# for sitemaps
from django.contrib.sitemaps.views import sitemap
from .sitemaps import PostSitemap
# for sitemaps End
sitemaps = {
    "posts":PostSitemap,
}

app_name = 'blog'

urlpatterns = [
    path('',views.home_redirect,name="home_redirect"),
    path('blog/list/',views.PostListView.as_view(),name="home"),
    path('blog/<str:category>/',views.posts_by_category,name="category"),
    path('blog/<str:category>/<slug:slug>/', views.post_detail, name='post_detail'),
    path('blog/contact-us',views.ContactUsView.as_view(), name="contact_us"),
    path('sitemap.xml',sitemap, {"sitemaps": sitemaps}, name="sitemap"),
    path('feed/rss/',LatestPostsFeed(), name="rss_feed"),
]
