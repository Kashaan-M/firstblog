from django.contrib import admin

from .models import Post,Comment

# Add summernote WYSIWYG model-start
from django_summernote.admin import SummernoteModelAdmin
# Add -end

# Register your models here.

# Previous: class PostAdmin(admin.ModelAdmin)
class PostAdmin(SummernoteModelAdmin):
    list_display = ['title','status','created_on']
    list_filter = ('status',)
    search_fields = ['title','content']
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ['content',]

admin.site.register(Post, PostAdmin)

# new syntax using python decorators

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['name','body','post','created_on','active']
    list_filter = ['active','created_on']
    search_fields = ['name','email','body']
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)

admin.site.site_header="Learn Economics"
admin.site.site_title = "Learn Economics"
admin.site.index_title=""