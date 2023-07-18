from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.db.models import Count
from django.shortcuts import render, get_object_or_404, redirect
# from django.core.paginator import Paginator
from django.urls import reverse_lazy
from django.views.decorators.http import require_POST
from django.views.generic import CreateView
from django.db import models

from .forms import RegistrationForm, PostSearchForm, LoginForm, PostForm, CommentForm
from .models import Post, Category, Like, Dislike, Comment


def index(request):
    title = 'Главная страница'
    categories = Category.objects.all()
    most_liked_post = Post.objects.annotate(num_likes=Count('like')).order_by('-num_likes').first()
    latest_posts = Post.objects.filter(is_published = True).order_by('-publish_date')[:2]
    context = {
        'title': title,
        'categories': categories,
        'most_liked_post': most_liked_post,
        'latest_posts': latest_posts
               }
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
    comments = Comment.objects.filter(post=post).order_by('-created_at')
    comment_form = CommentForm()
    
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.user = request.user
            new_comment.post = post
            new_comment.save()
            return redirect('post_detail', slug = slug)
    
    return render(request, 'Blog/Additional/post_detail.html', {'post': post, 'comments': comments, 'comment_form': comment_form})

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


def like_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    like, created = Like.objects.get_or_create(user=request.user, post=post)
    if not created:
        like.liked = not like.liked
        like.save()
    return redirect('post_detail', slug=post.slug)

# def most_liked_post(request):
#     most_liked_post = Post.objects.filter(likes_count__gt = 0).order_by('-likes_count').first()
#     return render(request, 'Blog/Info/posts.html', {'most_liked_post':most_liked_post})


def dislike_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    dislike, created = Dislike.objects.get_or_create(user=request.user, post=post)
    if not created:
        dislike.disliked = not dislike.disliked
        dislike.save()
    return redirect('post_detail', slug=post.slug)


@login_required
def delete_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    
    if request.user == post.author:
        post.delete()
    return redirect('posts')