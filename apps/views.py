from django.shortcuts import render
from .models import *
from django.contrib import messages
from datetime import datetime

# LOGIN, LOGOUT, REGISTER
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .models import Question, Response
from .forms import RegisterUserForm, LoginForm, NewQuestionForm, NewResponseForm, NewReplyForm

# Create your views here.

# MAIN HOME PAGE
def index(request):
    return render(request, "index.html")

# LOGIN, LOGOUT, REGISTER
def registerPage(request):
    form = RegisterUserForm()

    if request.method == 'POST':
        try:
            form = RegisterUserForm(request.POST)
            if form.is_valid():
                user = form.save()
                login(request, user)
                return redirect('classes')
        except Exception as e:
            print(e)
            raise

    context = {
        'form': form
    }
    return render(request, 'register.html', context)

def loginPage(request):
    form = LoginForm()

    if request.method == 'POST':
        try:
            form = LoginForm(data=request.POST)
            if form.is_valid():
                user = form.get_user()
                login(request, user)
                return redirect('classes')
        except Exception as e:
            print(e)
            raise

    context = {'form': form}
    return render(request, 'login.html', context)

@login_required(login_url='register')
def logoutPage(request):
    logout(request)
    return redirect('login')

@login_required(login_url='register')
def newQuestionPage(request):
    form = NewQuestionForm()

    if request.method == 'POST':
        try:
            form = NewQuestionForm(request.POST)
            if form.is_valid():
                question = form.save(commit=False)
                question.author = request.user
                question.save()
                return redirect('classes')
        except Exception as e:
            print(e)
            raise

    context = {'form': form}
    return render(request, 'new-question.html', context)

def classes(request):
    questions = Question.objects.all().order_by('-created_at')
    context = {
        'questions': questions
    }
    return render(request, 'classes.html', context)

def questionPage(request, id):
    response_form = NewResponseForm()
    reply_form = NewReplyForm()

    if request.method == 'POST':
        try:
            response_form = NewResponseForm(request.POST)
            if response_form.is_valid():
                response = response_form.save(commit=False)
                response.user = request.user
                response.question = Question(id=id)
                response.save()
                return redirect('/question/'+str(id)+'#'+str(response.id))
        except Exception as e:
            print(e)
            raise

    question = Question.objects.get(id=id)
    context = {
        'question': question,
        'response_form': response_form,
        'reply_form': reply_form,
    }
    return render(request, 'question.html', context)


@login_required(login_url='register')
def replyPage(request):
    if request.method == 'POST':
        try:
            form = NewReplyForm(request.POST)
            if form.is_valid():
                question_id = request.POST.get('question')
                parent_id = request.POST.get('parent')
                reply = form.save(commit=False)
                reply.user = request.user
                reply.question = Question(id=question_id)
                reply.parent = Response(id=parent_id)
                reply.save()
                return redirect('/question/'+str(question_id)+'#'+str(reply.id))
        except Exception as e:
            print(e)
            raise

    return redirect('index')

# FOR ANIMES
def animes(request):
    post = Animesview.objects.all()
    print(post)
    return render(request, 'animes.html', {'post': post})
    # return HttpResponse(" this is JobUpdates page")

def animesview(request, ids):
    mypost = Animesview.objects.filter(post_id=ids)[0]
    print(mypost)
    mypost.save()
    return render(request, 'animesview.html', {'mypost': mypost})
    # return HttpResponse(" this is JobUpdatesView page")

def searchanimes(request):
    if request.method == "POST":
        searched = request.POST['searched']
        sanimes = Animesview.objects.filter(name_episode__contains=searched)
        return render(request, 'searchanimes.html', {'searched': searched, 'sanimes': sanimes})
    else:
        return render(request, 'searchanimes.html', {})

# FOR JOBS
def jobupdates(request):
    myposts = Jobupdatesview.objects.all()
    print(myposts)
    return render(request, 'jobupdates.html', {'myposts': myposts})
    # return HttpResponse(" this is JobUpdates page")

def jobupdatesview(request, id):
    post = Jobupdatesview.objects.filter(post_id=id)[0]
    print(post)
    post.save()
    return render(request, 'jobupdatesview.html', {'post': post})
    # return HttpResponse(" this is JobUpdatesView page")

# FOR CONTACT US
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        number = request.POST.get('number')
        desc = request.POST.get('desc')
        cont = Contactus(name=name, email=email, number=number, desc=desc)
        cont.save()
        messages.success(request, "YOUR MESSAGE SEND SUCCESSFULLY.")
    return render(request, "contact.html")

