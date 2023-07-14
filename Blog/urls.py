from django.urls import path
from . import views
from .views import user_posts

urlpatterns = [
	path('', views.index, name = 'index'),
	path('posts/', views.posts, name = 'posts'),
	path('forum/', views.forum, name = 'forum'),
	path('guides/', views.guides, name = 'guides'),
	path('posts/<int:id>', views.post_detail, name = 'post_detail'),
	path('user/posts/', user_posts, name='user_posts'),
]

