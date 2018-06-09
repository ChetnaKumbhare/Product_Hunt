from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django import forms
def signup(request):
    if request.method == 'POST':
        password=len(request.POST['inputPassword4'])
        if password<8 :
              return render(request, 'accounts/signup.html', {'error':'Password is too short'})

              if request.POST['inputPassword4'] == request.POST['inputPassword5']:
                  try:
                      user = User.objects.get(username=request.POST['username'])
                      return render(request, 'accounts/signup.html', {'error':'Username is already been taken'})
                  except User.DoesNotExist:
                      user=User.objects.create_user(request.POST['username'], password=request.POST['inputPassword4'])
                      auth.login(request,user)
                      return redirect('home')
              else:
                 return render(request, 'accounts/signup.html', {'error':'Password donot match.. !'})

    else:
        return render(request,'accounts/signup.html')


def login(request):
    if request.method == 'POST':
        user=auth.authenticate(username=request.POST['username'],password=request.POST['inputPassword4'])
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            return render(request,'accounts/login.html',{'error':'username or password is incorrect.'})
    else:
        return render(request,'accounts/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')
