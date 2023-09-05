'''AUTHS VIEWS'''

from django.shortcuts import render, redirect 
from django.views import View
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.contrib.auth import authenticate, login
from auths.forms.register_form import RegisterForm
from django.contrib.auth.decorators import login_required
from auths.forms.login_form import LoginForm
from django import forms
from auths.forms.profile_form import UserProfileForm  
from auths.models.my_user import MyUser


class LoginView(View):
    """
    User login.
    """

    def get(self, request: HttpRequest) -> HttpResponse:
        ...

    def post(self, request: HttpRequest) -> HttpResponse:
        ...


class RegisterView(View):
    """
    User login.
    """

    template_name = 'register.html'

    def get(self, request: HttpRequest) -> HttpResponse:
        form = RegisterForm()
        return render(
            request=request,
            template_name=self.template_name,
            context={
                'form': form
                }
            )

    def post(self, request: HttpRequest) -> HttpResponse:
        form = RegisterForm(request.POST)
        if form.is_valid():
            del form.cleaned_data['password2']
            MyUser.objects.create(**form.cleaned_data)
        return render(
            request=request,
            template_name=self.template_name,
            context={
                'form': form
                }
            )

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('profile') 
            else:
                form.add_error(None, 'неверные данные')
    else:
        form = LoginForm()
    
    return render(request, 'login.html', 
                  {'form': form}
                  )


@login_required
def profile(request):
    user = request.user
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile') 
    else:
        form = UserProfileForm(instance=request.user)
    
    return render(request, 'profile.html', {'form': form , 'user': user})