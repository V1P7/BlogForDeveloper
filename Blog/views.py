from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.shortcuts import render, get_object_or_404, redirect
# from django.core.paginator import Paginator
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.db import models

from .forms import RegistrationForm, PostSearchForm, LoginForm, PostForm
from .models import Post, Category

def index(request):
    title = 'Главная страница'
    categories = Category.objects.all()
    context = {'title': title, 'categories': categories}
    return render(request, 'Blog/Main/index.html', context)

def posts(request):
    form = PostSearchForm()
    posts = Post.objects.all()
    categories = Category.objects.all()
    # paginator = Paginator(posts, 6)  # Показывать по 6 объектов на странице
    title = 'Все посты'
    # page_number = request.GET.get('page')
    # page_obj = paginator.get_page(page_number)
    
    if 'search_query' in request.GET:
        search_query = request.GET.get('search_query')
        # Выполните поиск по заголовку и содержимому
        posts = Post.objects.filter(
            models.Q(title__icontains = search_query) | models.Q(content__icontains = search_query)
        )
    # снять коммент когда придумаю как починить пагинацию
    # context = {'title': title, 'page_obj': page_obj, 'categories': categories, 'posts': posts, 'form': form}
    context = {'title': title, 'categories': categories, 'posts': posts, 'form': form}
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
    form_class = LoginForm
    def get_success_url(self):
        return reverse_lazy('index')

def logout_user(request):
    logout(request)
    return redirect('login')

@login_required
def create_post(request):
    # title = 'Написать статью'
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, user=request.user)
        if form.is_valid():
            form.instance.author = request.user
            form.save()
            return redirect('posts')
    else:
        form = PostForm(user=request.user)
        
        # context = {'title': title, 'form': form}
        return render(request, 'Blog/Additional/create_post.html', {'form': form})
        