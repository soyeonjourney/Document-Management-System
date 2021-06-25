from django.shortcuts import render, redirect
from django.views.generic.base import View
import hashlib

from .models import User, EmailVerification
from .forms import RegisterForm, LoginForm
from utils.send_email import send_register_email


def register(request):
    if request.session.get('is_login', None):
        return redirect('/home')
    
    if request.method == 'POST':
        register_form = RegisterForm(request.POST)
        message = "All info should be filled in"
        if register_form.is_valid():
            username = register_form.cleaned_data['username']
            password1 = register_form.cleaned_data['password1']
            password2 = register_form.cleaned_data['password2']
            email = register_form.cleaned_data['email']
            if password1 != password2:
                message = "Different password input"
                return render(request, 'users/register.html', {'message': message, 'register_form': register_form})
            else:
                duplicated_username = User.objects.filter(name=username)
                if duplicated_username:
                    message = "Username already exist"
                    return render(request, 'users/register.html', {'message': message, 'register_form': register_form})
                else:
                    duplicated_email = User.objects.filter(email=email)
                    if duplicated_email:
                        message = "E-mail already exist"
                        return render(request, 'users/register.html', {'message': message, 'register_form': register_form})
                    else:
                        new_user = User.objects.create()
                        new_user.name = username
                        new_user.password = hash_pwd(password1)
                        new_user.email = email
                        new_user.save()
                        send_register_email(email)
                        return redirect('/user/login')

    register_form = RegisterForm()
    return render(request, 'users/register.html', {'register_form': register_form})


def login(request):
    if request.session.get('is_login', None):
        return redirect('/home')

    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        message = "All info should be filled in"
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            try:
                user = User.objects.get(name=username)
                if user.is_active:
                    if hash_pwd(password) == user.password:
                        request.session['is_login'] = True
                        request.session['user_id'] = user.id
                        request.session['user_name'] = user.name.title()
                        return redirect('/home')
                    else:
                        message = "Password not corrected"
                else:
                    message = "User not activate"
            except:
                message = "User not exist"
        return render(request, 'users/login.html', {'message': message, 'login_form': login_form})

    login_form = LoginForm()
    return render(request, 'users/login.html', {'login_form': login_form})


def logout(request):
    if not request.session.get('is_login', None):
        return redirect('/home')
    
    request.session.flush()
    # Or method below
    # del request.session['is_login']
    # del request.session['user_id']
    # del request.session['user_name']
    return redirect('/home')


class ActiveUser(View):
    def get(self, request, active_code):
        # Get all records of the active_code
        all_records = EmailVerification.objects.filter(code=active_code)
        for record in all_records:
            # Activate one by one
            user = User.objects.get(email=record.email)
            user.is_active = True
            user.save()
        return redirect('/user/login')


def hash_pwd(pwd, salt='lilac4cvpr'):
    return hashlib.sha256(salt.encode() + pwd.encode()).hexdigest()
