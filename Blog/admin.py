from django.contrib import admin
from .models import Post, Category

def public_all(modeladmin, request, queryset):
	queryset.update(is_published=True)
public_all.short_description = 'Опубликовать все посты'
class PostAdmin(admin.ModelAdmin):
	list_display = ('title', 'author', 'publish_date', 'get_categories')
	list_filter = ('author', 'publish_date')
	search_fields = ('title', 'content')
	
	def get_categories(self, obj):
		return ', '.join([category.name for category in obj.categories.all()])
	get_categories.short_description = 'Категории'
	
admin.site.register(Post, PostAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']  # Отображение поля name в списке объектов

admin.site.register(Category, CategoryAdmin)