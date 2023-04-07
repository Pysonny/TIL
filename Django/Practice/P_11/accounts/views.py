from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth import update_session_auth_hash



# Create your views here.
def login(request):
    if request.user.is_authenticated:
        return redirect('articles:index')

    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('articles:index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)


def logout(request):
    auth_logout(request)
    return redirect('articles:index')


def signup(request):
    if request.user.is_authenticated:
        return redirect('articles:index')
    
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)


def delete(request):
   # 유저 삭제
   request.user.delete()
   # 세션 삭제 ( 필수 아님 )
   auth_logout(request)
   return redirect('articles:index')


def update(request):
   if request.method == 'POST':
      form = CustomUserChangeForm(request.POST, instance=request.user) # 수정엔 instance가 들어감
      if form.is_valid():
         form.save()
         return redirect('articles:index')
   else:
      form = CustomUserChangeForm(instance=request.user)
   context = {
      'form' : form,
   }
   return render(request, 'accounts/update.html', context)


def change_password(request):
   if request.method == 'POST':
      form = PasswordChangeForm(request.user, request.POST)
      if form.is_valid():
         user = form.save()
         # 비밀번호 변경시 세션 무효화 방지
         update_session_auth_hash(request, user)
         return redirect('articles:index')
   else:
      form = PasswordChangeForm(request.user) # request.user 필수로 넣기
   context = {
      'form': form,
   }
   return render(request, 'accounts/change_password.html', context)