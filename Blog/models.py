from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify

class Post(models.Model):
	title = models.CharField(verbose_name = 'Оглавление', max_length=50)
	content = models.TextField(verbose_name = 'Содержание поста')
	author = models.ForeignKey(User, verbose_name = 'Автор', on_delete = models.CASCADE, related_name = 'posts')
	photo = models.ImageField(verbose_name = 'Изображение', upload_to = 'media/%Y', blank = True)
	read_time = models.PositiveIntegerField(verbose_name = 'Время прочтения в минутах')
	publish_date = models.DateTimeField(verbose_name = 'Дата публикации', default = timezone.now)
	updated_date = models.DateTimeField(verbose_name = 'Дата последнего обновления', auto_now = True)
	is_published = models.BooleanField(verbose_name = 'Опубликовано', default = False)
	#slug = models.SlugField(verbose_name = 'Читаемый URL', unique = True, default='')
	
	class Meta:
		verbose_name = 'Пост'
		verbose_name_plural = 'Посты'
	
	# def save(self, *args, **kwargs):
	# 	if not self.slug:  # Проверка, чтобы не перезаписывать уже существующий slug
	# 		words = self.title.split()[:3]  # Получение первых трех слов из заголовка
	# 		self.slug = slugify(' '.join(words))
	# 	super().save(*args, **kwargs)
		
	def __str__(self):
		return self.title