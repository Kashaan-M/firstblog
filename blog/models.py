from django.db import models
from django.contrib.auth.models import User
from django_summernote.fields import SummernoteTextField
from django.urls import reverse

# Create your models here.

STATUS = (
    (0, "Default"),
    (1, "Publish")
)
CATEGORY = {
    "Economics": "Economics",
    "Chemistry": "Chemistry",
    "Physics": "Physics",
    "Maths": "Maths"
}


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    category = models.CharField(choices=CATEGORY, max_length=9, default="Economics")
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now=True)
    content = SummernoteTextField()
    banner = models.ImageField(default="fallback.png", blank=True) # blank=True means if we don't provide an image then that is ok
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("blog:post_detail", kwargs={"slug": str(self.slug)})
    
            
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=200)
    email = models.EmailField()
    body = SummernoteTextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active =  models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)
