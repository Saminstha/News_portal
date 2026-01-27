from django.contrib import admin
from newspaper.models import Post, Category, Tag, Advertisement, Contact, OurTeam, UserProfile, Comment, Newsletter
from django import forms
from tinymce.widgets import TinyMCE
from unfold.admin import ModelAdmin

# Register your models here.
#admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Advertisement)
admin.site.register(Contact)
admin.site.register(OurTeam)
admin.site.register(UserProfile)
admin.site.register(Comment)
admin.site.register(Newsletter)


class PostAdminForm(forms.ModelForm):
    content= forms.CharField(widget=TinyMCE())
    
    class Meta:
        model= Post
        fields= '__all__'
        
@admin.register(Post)
class PostAdmin(ModelAdmin):
    form= PostAdminForm
    
    date_hierarchy= 'published_at'
    list_display= [
        'title',
        'author',
        'published_at',
        'category',
        'is_breaking_news'
    ]
    search_fields = (
        'title',
        'content',
        'author__username',
        'category__name',
        'tag__name',
    )
    
    