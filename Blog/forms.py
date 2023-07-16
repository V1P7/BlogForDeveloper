from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class RegistrationForm(UserCreationForm):
	email = forms.EmailField(label = 'Почта')
	username = forms.CharField(label = 'Никнейм')
	password1 = forms.CharField(label = 'Пароль', widget = forms.PasswordInput)
	password2 = forms.CharField(label = 'Подтвердите пароль', widget = forms.PasswordInput)
	
	class Meta:
		model = User
		fields = ['email', 'username', 'password1', 'password2']
		
		
class LoginForm(AuthenticationForm):
	username = forms.CharField(
		widget = forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'Имя пользователя'})
	)
	password = forms.CharField(
		widget = forms.PasswordInput(attrs = {'class': 'form-control', 'placeholder': 'Пароль'})
	)
class PostSearchForm(forms.Form):
	search_query = forms.CharField(label = '', max_length = 100)