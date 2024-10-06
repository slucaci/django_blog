from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin

"""
Admin configuration for the Post model.
Uses Django Summernote for rich text editing on the 'content' field.
"""
@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    """
    Configuration for how the Post model appears in the admin panel.
    
    - list_display: Columns to display in the post list view.
    - search_fields: Fields that can be searched in the admin panel.
    - list_filter: Fields to filter the post list.
    - prepopulated_fields: Automatically populate the slug field based on the title.
    - summernote_fields: Fields that should use the Summernote editor.
    """
    list_display = ('title', 'slug', 'status')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)

"""
Registers the Comment model in the Django admin panel.
"""
admin.site.register(Comment)
