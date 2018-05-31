from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages


def index(request):
    return render(request, 'user_app/index.html')

def register(request):
    user = User.userManager.register(request.POST['username'], request.POST['email'], request.POST['password'], request.POST['confirm_password'])
    if user[0]:
        request.session['user_id'] = user[1].id
        request.session['username'] = user[1].username

        return redirect('/home')

    else:
        for error in user[1]:
            messages.add_message(request, messages.ERROR, error)
        return redirect('/')


def login(request):
    user = User.userManager.login(request.POST['email'], request.POST['password'])
    if user[0]:
        request.session['user_id'] = user[1].id
        request.session['username'] = user[1].username

        return redirect('/home')
    else:
        for error in user[1]:
            messages.add_message(request, messages.ERROR, error)
        return redirect('/')


def logout(request):
    request.session.clear()
    return redirect('/')