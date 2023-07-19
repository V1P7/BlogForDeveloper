from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.utils import timezone
from django.utils.text import slugify


class Category(models.Model):
	name = models.CharField(max_length = 200)
	
	def __str__(self):
		return self.name
	
	class Meta:
		verbose_name = 'категорию'
		verbose_name_plural = 'Категории'


class Post(models.Model):
	title = models.CharField(verbose_name = 'Оглавление', max_length = 50)
	content = models.TextField(verbose_name = 'Содержание поста')
	author = models.ForeignKey(User, verbose_name = 'Автор', on_delete = models.CASCADE, related_name = 'posts')
	photo = models.ImageField(verbose_name = 'Изображение', upload_to = 'media/%Y', blank = True)
	read_time = models.PositiveIntegerField(verbose_name = 'Время прочтения в минутах')
	publish_date = models.DateTimeField(verbose_name = 'Дата публикации', default = timezone.now)
	updated_date = models.DateTimeField(verbose_name = 'Дата последнего обновления', auto_now = True)
	is_published = models.BooleanField(verbose_name = 'Опубликовано', default = False)
	slug = models.SlugField(verbose_name = 'Читаемый URL', unique = True, default = '', null = True, blank = True)
	categories = models.ManyToManyField(Category, verbose_name = 'Категории', null = True, blank = True)
	likes_count = models.IntegerField(default = 0, verbose_name = 'Количество лайков')
	
	class Meta:
		verbose_name = 'Пост'
		verbose_name_plural = 'Посты'
	
	def save(self, *args, **kwargs):
		if not self.pk:  # Проверка, чтобы не перезаписывать уже существующий slug
			words = self.title.split()[:3]  # Получение первых трех слов из заголовка
			self.slug = slugify(' '.join(words))
		super().save(*args, **kwargs)
	
	def __str__(self):
		return self.title
	
	def count_likes(self):
		return self.like_set.filter(liked = True).count()
	
	def count_dislikes(self):
		return self.dislike_set.filter(disliked = True).count()


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey('Blog.Post', on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='replies')

    def __str__(self):
        return f'{self.user.username} - {self.text}'


class Like(models.Model):
	user = models.ForeignKey(User, on_delete = models.CASCADE)
	post = models.ForeignKey(Post, on_delete = models.CASCADE)
	liked = models.BooleanField(default = True)
	
	def save(self, *args, **kwargs):
		if self.liked:
			self.post.likes_count += 1
		else:
			self.post.likes_count -= 1
		self.post.save()
		super().save(*args, **kwargs)


class Dislike(models.Model):
	user = models.ForeignKey(User, on_delete = models.CASCADE)
	post = models.ForeignKey(Post, on_delete = models.CASCADE)
	disliked = models.BooleanField(default = True)


class Subscriber(models.Model):
	email = models.EmailField(unique = True)
	
	def __str__(self):
		return self.email