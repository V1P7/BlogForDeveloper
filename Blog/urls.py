from django.urls import path
from . import views
from .views import user_posts, posts_by_category, RegisterUser, LoginUser, logout_user, create_post

urlpatterns = [
	path('', views.index, name = 'index'),
	
	path('forum/', views.forum, name = 'forum'),
	path('guides/', views.guides, name = 'guides'),
	path('posts/', views.posts, name = 'posts'),
	
	path('posts/<slug:slug>', views.post_detail, name = 'post_detail'),
	path('user/posts/<int:user_id>/', user_posts, name='user_posts'),
	path('category/<int:category_id>/', posts_by_category, name='posts_by_category'),
	path('create_post/', create_post, name='create_post'),
	
	path('like_post/<int:post_id>/', views.like_post, name = 'like_post'),
	path('dislike_post/<int:post_id>/', views.dislike_post, name = 'dislike_post'),
	
	path('login/', LoginUser.as_view(), name='login'),
	path('register/', RegisterUser.as_view(), name='register'),
	path('logout/', logout_user, name='logout'),
]

