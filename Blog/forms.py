from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistrationForm(UserCreationForm):
	email = forms.EmailField(label = 'Почта')
	username = forms.CharField(label = 'Никнейм')
	password1 = forms.CharField(label = 'Пароль', widget = forms.PasswordInput)
	password2 = forms.CharField(label = 'Подтвердите пароль', widget = forms.PasswordInput)
	
	class Meta:
		model = User
		fields = ['email', 'username', 'password1', 'password2']