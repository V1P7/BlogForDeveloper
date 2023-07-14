from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .models import Post, Category

@login_required

def index(request):
	title = 'Главная страница'
	categories = Category.objects.all()
	context = {'title': title, 'categories': categories}
	return render(request, 'Blog/Main/index.html', context)

def posts(request):
	title = 'Заглушка для постов'
	posts = Post.objects.all()
	categories = Category.objects.all()
	paginator = Paginator(posts, 6) # Показывать по 6 объектов на странице
	
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)
	
	context = {'title': title, 'page_obj': page_obj, 'categories': categories}
	
	return render(request, 'Blog/Info/posts.html', context)

def forum(request):
	title = 'Заглушка для форума'
	context = {'title': title}
	return render(request, 'Blog/Info/forum.html', context)

def guides(request):
	title = 'Заглушка для гайдов'
	context = {'title': title}
	return render(request, 'Blog/Info/guides.html', context)

def post_detail(request, slug):
	post = get_object_or_404(Post, slug=slug)
	return render(request, 'Blog/Additional/post_detail.html', {'post': post})

def user_posts(request):
    user = request.user  # Получаем текущего пользователя
    title = 'Все статьи пользователя'
    posts = Post.objects.filter(author=user)
    context = {'title': title, 'posts': posts}
    return render(request, 'Blog/Additional/user_posts.html', context)

def posts_by_category(request, category_id):
    category = Category.objects.get(id=category_id)
    posts = Post.objects.filter(categories=category)
    context = {'category': category, 'posts': posts}
    return render(request, 'Blog/Additional/category_posts.html', context)