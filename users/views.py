from django.views.generic import View
from django.shortcuts import render, redirect
from users.forms import LoginForm, UserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, AnonymousUser
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class LoginView( View ):
	template_name = 'registration/login.html'
	authetication_form = LoginForm
	redirect_field_name = 'registration/success.html'
	current_app = 'users'


	def get(self, request):
		return render(request, self.template_name, {'form':self.authetication_form})

class IndexView(View):
	def get(self, request):
		if request.user.is_anonymous():
			return render( request, 'registration/login.html', {"form":AuthenticationForm()} )
		else:
			return render(request, 'login.html')

class LogoutView( View ):


	def get(self, request):
		pass

	def post(self, request):
		pass

class SignupView( View ):


	def get(self, request):
		return render(request, 'registration/register.html', {'form':UserCreationForm()})

	def post(self, request):
		pass

class RegisterView( View ):
	template_name = 'registration/register.html'

	def post(self, request):
		username = request.POST['username']
		password = request.POST['password1']
		user = User.objects.create(username=username, password=password)
		user.set_password(password)
		user = authenticate(username=username, password=password)
		print('this is user', user)
		if user is not None:
			if user.is_active:
				login(request, user)
				return redirect('/users/')
		else:
			return redirect('/users/register', {'errors':'Sorry try again!'})

class SuccessView( View ):
	template_name = 'registration/success.html'
	
	def get(self, request):
		return render(request, self.template_name)