from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Post, Comment


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(label='Почта', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Почта'}))
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Логин'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Пароль'}))
    password2 = forms.CharField(label='Подтвердите пароль', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Подтвердите пароль'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
		
		
class LoginForm(AuthenticationForm):
	username = forms.CharField(label='Логин', widget = forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'Логин'}))
	password = forms.CharField(label='Пароль', widget = forms.PasswordInput(attrs = {'class': 'form-control', 'placeholder': 'Пароль'}))
class PostSearchForm(forms.Form):
	search_query = forms.CharField(label='Поиск', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Поиск'}))
	
class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ['title', 'content', 'photo', 'read_time', 'categories']
		
	def __init__(self, *args, **kwargs):
		self.user = kwargs.pop('user', None)
		super().__init__(*args, **kwargs)
		self.fields['title'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Оглавление'})
		self.fields['content'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Содержание поста'})
		self.fields['photo'].widget.attrs.update({'class': 'form-control'})
		self.fields['read_time'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Время прочтения в минутах'})
		self.fields['categories'].widget.attrs.update({'class': 'form-control'})
		
	def save(self, commit=True):
		if self.user:
			self.instance.author = self.user
		return super().save(commit=commit)


class CommentForm(forms.ModelForm):
	# text = forms.CharField(label = 'Текст')
	class Meta:
		model = Comment
		fields = ['text']
	def __init__(self, *args, **kwargs):
		self.user = kwargs.pop('user', None)
		super().__init__(*args, **kwargs)
		self.fields['text'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Текст комментария'})
		