from django.urls import path
from . import views
from .views import user_posts, posts_by_category

urlpatterns = [
	path('', views.index, name = 'index'),
	path('posts/', views.posts, name = 'posts'),
	path('forum/', views.forum, name = 'forum'),
	path('guides/', views.guides, name = 'guides'),
	path('posts/<slug:slug>', views.post_detail, name = 'post_detail'),
	path('user/posts/', user_posts, name='user_posts'),
	path('category/<int:category_id>/', posts_by_category, name='posts_by_category'),
]

