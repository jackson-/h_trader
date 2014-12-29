from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

class UserForm( UserCreationForm ):
	username = forms.CharField(max_length=50)
	email = forms.EmailField()
	# password = forms.CharField(max_length=50)

	class Meta:
		model = User
		fields = ('username', 'email')

class LoginForm( AuthenticationForm ):
	class Meta:
		model = User
		fields = ('username', 'password', 'email')

	def confirm_login_allowed(self, user):
		pass