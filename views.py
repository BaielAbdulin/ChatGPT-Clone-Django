from django.shortcuts import render, redirect
# from django.http import HttpResponse
from .forms import CreateUserForm, LoginForm
from .models import Message
from .chatgpt import chatgpt_answer
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.

# Home Page
def home(request):
    return render(request, 'home.html')

# SignUp Page
def signup(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)

        # If form is valid, log user in and redirect to chatbot
        if form.is_valid():
            form.save()
            username = request.POST.get('username')
            password = request.POST.get('password1')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth.login(request, user)
                return redirect('chatbot')

    context = {'signupform': form}

    return render(request, 'signup.html', context=context)

# Login Page
def login(request):
    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)

        # If form is valid, log user in and redirect to chatbot
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth.login(request,user)

                return redirect('chatbot')

    context = {'loginform': form}

    return render(request, 'login.html', context=context)

# Logout Request
def logout(request):
    auth.logout(request)
    return redirect('home')

# Chatbot Page
@login_required(login_url="/login")
def chatbot(request):
    if request.method == 'POST':

        # If request is for a new message
        if "new-message" in request.POST:
            user = request.user
            messages = list(Message.objects.filter(user=user).order_by('timestamp'))
            question = request.POST.get('chat-input').strip()

            if question:
                answer = chatgpt_answer(messages, question)
                Message.objects.create(user=user, question=question, answer=answer)

        # If request is to delete a message
        elif "delete-message" in request.POST:
            message_id = request.POST.get("delete-message")
            Message.objects.filter(id=message_id).delete()

        # Redirect for Get request
        return redirect('chatbot')

    # Get Request
    messages = list(Message.objects.filter(user=request.user).order_by('timestamp'))
    context = {'messages': messages}

    return render(request, 'chatbot.html', context=context)