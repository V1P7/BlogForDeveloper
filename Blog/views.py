from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	title = 'Главная страница'
	context = {'title': title}
	return render(request, 'Blog/Main/index.html', context)

def posts(request):
	title = 'Заглушка для постов'
	context = {'title': title}
	return render(request, 'Blog/Info/posts.html', context)

def forum(request):
	title = 'Заглушка для форума'
	context = {'title': title}
	return render(request, 'Blog/Info/forum.html', context)

def guides(request):
	title = 'Заглушка для гайдов'
	context = {'title': title}
	return render(request, 'Blog/Info/guides.html', context)