from django.urls import path
from Blog import views
from .views import user_posts, posts_by_category, RegisterUser, LoginUser, logout_user, create_post

urlpatterns = [
	#   Отображение главной страницы
	path('', views.index, name = 'index'),
	# Отображение страниц с постами и т.д
	path('forum/', views.forum, name = 'forum'),
	path('guides/', views.guides, name = 'guides'),
	path('posts/', views.posts, name = 'posts'),
	#   Отображение постов и дейстия с ними
	path('posts/<slug:slug>', views.post_detail, name = 'post_detail'),
	path('user/posts/<int:user_id>/', user_posts, name='user_posts'),
	path('category/<int:category_id>/', posts_by_category, name='posts_by_category'),
	path('create_post/', create_post, name='create_post'),
	path('delete_post/<slug:slug>/', views.delete_post, name='delete_post'),
	#   Отображение лайков дизлайков
	path('like_post/<int:post_id>/', views.like_post, name = 'like_post'),
	path('dislike_post/<int:post_id>/', views.dislike_post, name = 'dislike_post'),
	path('comment/<int:comment_id>/like/', views.add_like_to_comment, name='add_like_to_comment'),
	path('add_reply/<int:comment_id>/', views.add_reply, name='add_reply'),
	# path('most_like_post/<int:post_id>/', views.most_liked_post, name = 'most_liked_post'),
	#   Отображение страниц входа/регистрации/выхода
	path('login/', LoginUser.as_view(), name='login'),
	path('register/', RegisterUser.as_view(), name='register'),
	path('logout/', logout_user, name='logout'),
	#   Отображение страницы успешной подписки
	path('success/', views.success, name='success'),
	
]

