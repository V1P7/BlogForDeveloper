from django.contrib import admin
from .models import Post

def public_all(modeladmin, request, queryset):
	queryset.update(is_published=True)
public_all.short_description = 'Опубликовать все посты'
class PostAdmin(admin.ModelAdmin):
	list_display = ('title', 'author', 'publish_date')
	list_filter = ('author', 'publish_date')
	search_fields = ('title', 'content')
	
admin.site.register(Post, PostAdmin)