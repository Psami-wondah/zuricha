
import json
from django.utils.safestring import mark_safe
from django.shortcuts import render, redirect

from django.contrib.auth import login, logout, authenticate

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# Create your views here.


def index(request):
    return render(request, 'chat/index.html', {})

@login_required()
def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name': room_name,
        'username': mark_safe(json.dumps(request.user.username)),
    })

def homepage(request):
    return render(request, 'chat/login.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm
    return render(request, 'chat/register.html', {'form': form})

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)

            if user is not None:

                login(request, user)
                messages.info(request, f'You are now logged in as {username}')
                return redirect('index')
            else:
                messages.error(request, 'Invalid username or password')
        else:
            messages.error(request, 'Invalid username or password.')
    form = AuthenticationForm()
    return render(request=request, template_name='chat/login.html', context={'login_form': form})


def logout_request(request):
    logout(request)
    messages.info(request, "You have sucessfully logged out.")
    return redirect("login")