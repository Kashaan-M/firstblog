from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords
from .models import Post
from django.urls import reverse

class LatestPostsFeed(Feed):
    title="Learn Economics"
    link=""
    description = "New posts on Learn Economics"

    def items(self):
        return Post.objects.filter(status=1)
    
    def item_title(self,item):
        return item.title
    
    def item_description(self,item):
        return truncatewords(item.content, 30)

    
    # Only needed if the model has no get_absolute_url method
    # def item_link(self, item):
    #     return reverse("post_detail", args=[item.slug])