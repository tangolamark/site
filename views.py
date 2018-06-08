from django.contrib.auth import authenticate, logout, login, get_user
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from django.contrib.auth import get_user_model
User = get_user_model()

# Create your views here.
from django.views.generic import ListView, UpdateView

from main.form import SignUpForm, UpdateProfile
from main.models import Topic, Subtopic, Data, Test, Question, Course


def courseview(request):
    course = Course.objects.all()
    return render(request, 'course.html', {'Course': course})

def topicview(request, id):
    if request.user.is_authenticated:
        topic = Topic.objects.filter(course=id)
        subtopic = Subtopic.objects.all()
        return render(request, 'topic.html', {'Topic': topic, 'Subtopic': subtopic, 'username': get_user(request).username})
    else:
        return redirect('LogIn')

# def topicview(request):
#     topics = Topic.objects.all()
#     subtopics = Subtopic.objects.all()
#     return render(request, 'index.html', {'TopicList': topics, 'SubtopicList': subtopics})

# def datalist(request):
#     data = Data.objects.all()
#     return render(request,'detail.html', {'DataList': data})

def testview(request):
    test = Test.objects.all()
    return render(request, 'alltest.html', {'Test': test, 'username': get_user(request).username})

def quesview(request, id):
    if request.user.is_authenticated:
        question = Question.objects.filter(test=id)
        return render(request, 'test.html', {'Question': question, 'username': get_user(request).username})
    else:
        return redirect('LogIn')

# def topicdataview(request, id):
#     if request.user.is_authenticated:
#         data = Data.objects.filter(topic=id)
#         return render(request, 'detail.html', {'Topic': data, 'username': get_user(request).username})
#     else:
#         return redirect('LogIn')

def dataview(request, id):
    if request.user.is_authenticated:
        data = Data.objects.filter(subtopic=id)
        subtopic = Subtopic.objects.filter(pk=id)
        #data = Data.objects.all()
        #data = Data.objects.get_queryset().filter(pk=id)
        return render(request, 'detail.html', {'Subtopic': data, 'Back': subtopic, 'username': get_user(request).username})
    else:
        return redirect('LogIn')
    #'username':get_user(request).username

def logout_view(request):
    logout(request)
    return redirect('LogIn')

def log(request):
    args = {}
    username = request.POST.get('username')#['username']
    password = request.POST.get('password')#['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return redirect('Course')
        else:
            args['login_error'] = "Неверный логин/пароль"
            return render(request, 'auth.html', args)

    else:
        return render(request, 'auth.html', args)

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('Course')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def startcourse(request, id):
    if request.user.is_authenticated:
        course = Course.objects.filter(pk=id)
        # if course:
        course.title = 'a'
        course.save()
        # Course.objects.filter(pk=id).update(is_used=True)
        # Course.save()
        # for i in range(len(Course)):
        #     if Course[i].pk == id:
        #         Course[i].is_used = True
        #         Course[i].save()
        # return render(request, 'topic.html', {'username': get_user(request).username})
    else:
        return redirect('LogIn')

def update_profile(request):
    args = {}
    if request.method == 'POST':
        # us = User.objects.filter(pk=1)
        form = UpdateProfile(request.POST, instance=request.user)
        # , initial = {'username': 'abc', 'email': 'abc@abc.abc', 'first_name': 'abc', 'last_name': 'abc'}
        # form.actual_user = request.user
        if form.is_valid():
            form.save()
            return redirect('Profile')
    else:
        form = UpdateProfile(instance=request.user)

    args['form'] = form
    return render(request, 'profile.html', args)