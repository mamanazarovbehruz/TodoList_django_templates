from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from company.models import Company
from .models import *
from .forms import *

# Create your views here.

# def login_user(request):
#     form = UserLoginForm()
#     if request.method == 'POST':
#         form = UserLoginForm(request.POST)
#         print(form)
#         if form.is_valid():
#             try:
#                 user = authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password'])
#             except:
#                 user = None
#             if user and user.is_active:
#                 login(request, user)
#                 return redirect('home')
#         else:
#             print('Forma xato to\'ldirilgan!') 
#     context = {
#         'form': form
#     }
#     return render(request, 'login.html', context)

def login_user(request):
    form = UserLoginForm()
    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Foydalanuvchi topilmadi!')
    context = {
        'form': form
    }
    return render(request, 'login.html', context)


def register_user(request):
    form = UserRegisterForm
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = form.save(commit=False)
            if cd['password'] != cd['password1']:
                return redirect('register_user')
            else:
                user.set_password(cd['password1'])
                user.save()
                # profile = Profile(user=user)
                # profile.save()
                # company = Company(user=user)
                # company.save()
                return redirect('login_user')
    return render(request, 'register.html', {'form':form})

def update_account(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(instance=request.user, data=request.POST)
        profile_form = ProfilUpdateForm(instance=request.user.profil, data=request.POST, files=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('accounts:profile')
        else:
            messages.error(request, 'Formada xatolik bor!')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfilUpdateForm(instance=request.user.profil)
    context = {
        'user_form':user_form,
        'profile_form':profile_form,
    }
    return render(request, 'update.html', context)

def password_change(request):
    if request.method == 'POST':
        form = PassUpdateForm(request.POSt)
        if form.is_valid():
            user = User.objects.get(id=request.user.id)
            if user.check_password(form.cleaned_data['password']):
                user.set_password(form.cleaned_data['password2'])
                user.save()
                return redirect('profile')
            else:
                messages.error(request, 'Eski parolni xato kiritingiz!')
                return redirect('password_change')
        else:
            messages.error(request, 'Formada xatolik bor!')
            return redirect('password_change')
    else:
        form = PassUpdateForm()
    return render(request, 'password_change.html', {'form':form})

def user_logout(request):
    logout(request)
    return redirect('task:index')

def user_delete(request):
    user = User.objects.get(id=request.user)
    profile = Profile.objects.get(id=request.user)
    user.delete()
    profile.delete()
    return redirect('task:index')

@login_required
def home(request):
    return render(request, 'home.html')