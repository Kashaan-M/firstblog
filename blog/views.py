from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from django.views import generic,View
from .models import Post
from .forms import CommentForm

# pagination using view function
from django.core.paginator import Paginator
# pagination END

# Create your views here.

class PostListView(generic.ListView):
    queryset = Post.objects.filter(status=1)
    paginate_by = 2
    template_name = "index.djhtml"
    
def home_redirect(request):
    return HttpResponseRedirect('blog/list/')

def post_detail(request,category, slug):
    template_name = 'post_detail.djhtml'
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True)
    new_comment = None # comment posted

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()
    return render(request, template_name, {
        'post':post,
        'comments': comments,
        'new_comment': new_comment,
        'comment_form': comment_form
        })

def posts_by_category(request,category):
    if request.method == "GET":
        category = category
        page_number = request.GET.get('page','')
        if category == '' or page_number == '':
            posts_by_category_list = Post.objects.all()
        
        posts_by_category_list = Post.objects.filter(category=category)

        paginator = Paginator(posts_by_category_list, 2)
        post_list = paginator.get_page(page_number)


        return render(request,'posts_by_category_list.djhtml',{'post_list':post_list,'category':category})
    

class ContactUsView(View):
    def get(self,request):
        return HttpResponse("Contact Us")

