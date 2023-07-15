from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import RegistrationForm
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

def user_posts(request, user_id):
    user = User.objects.get(id=user_id)
    title = 'Все статьи пользователя'
    posts = Post.objects.filter(author=user)
    context = {'title': title, 'posts': posts}
    return render(request, 'Blog/Additional/user_posts.html', context)

def posts_by_category(request, category_id):
    category = Category.objects.get(id=category_id)
    posts = Post.objects.filter(categories=category)
    title = 'Все посты в категории: '
    context = {'category': category, 'posts': posts, 'title': title}
    return render(request, 'Blog/Additional/category_posts.html', context)

class RegisterUser(CreateView):
	form_class = RegistrationForm
	template_name = 'Blog/Additional/register.html'
	success_url = reverse_lazy('login')
	
	def form_valid(self, form):
		form.save()
		return super().form_valid(form)
	
class LoginUser(LoginView):
    template_name = 'Blog/Additional/login.html'
    form_class = AuthenticationForm
    
    def get_success_url(self):
	    return reverse_lazy('index')

def LogoutUser(request):
	logout(request)
	return redirect('login')