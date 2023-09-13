from django.shortcuts import render, redirect
from .models import Todo
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.contrib import messages
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import TodoSerializer

# Create your views here.

def registerUser(request):
    form= UserCreationForm()
    if request.method== 'POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            return redirect('todo:register_completed')
        else:
            messages.add_message(request, messages.INFO, "Sorry! Something went wrong!!")

    context={'form':form}
    return render(request, 'login_register.html', context)



def loginPage(request):

    page='login'
    if request.user.is_authenticated:
        return HttpResponse('Sorry but you have already logged in!!')

    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        try:
            user=User.objects.get(username=username)
        except:
            messages.add_message(request, messages.INFO, "This user does'nt exist!!!")

        user=authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('todo:login_completed')
        else:
            messages.add_message(request, messages.INFO, " Username or password does'nt exist!!!")
    

    context={'page':page}
    return render(request, 'login_register.html', context= context)




def intro(request):
    return render(request, 'intro.html')

def loginCompleted(request):
    return render(request, 'login_completed.html')

def logouUser(request):
    logout(request)
    return redirect('todo:intro')

def registerCompleted(request):
    return render(request, 'register_completed.html')

@login_required(login_url='todo:login')
def index(request):
    
    todo=Todo.objects.all()
    if request.method=='POST':
        if request.POST['title']:

        
            if request.POST['priority'] and request.POST['date']:
                new_todo=Todo(
                    title=request.POST['title'],
                    priority=request.POST['priority'],
                    due_date=request.POST['date'],
                )

            elif request.POST['priority'] and not request.POST['date']:
                new_todo=Todo(
                    title=request.POST['title'],
                    priority=request.POST['priority'],
                
                )

            elif not request.POST['priority'] and  request.POST['date']:
                new_todo=Todo(
                    title=request.POST['title'],
                    due_date=request.POST['date'],
                
                )
            else:
                new_todo=Todo(
                    title=request.POST['title'],
                
                )
            new_todo.save()
            return redirect('todo:index')
        else:
            pass
    
    context={
        'todos':todo,
    }

    return render(request, 'index.html', context)

def delete(request, pk):
    todo=Todo.objects.get(id=pk)
    todo.delete()
    return redirect('todo:index')

class TodoApi(APIView):
    def get(self , request, format= None):
        todo=Todo.objects.all()
        serializer=TodoSerializer(todo, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer=TodoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(request.data, status= status.HTTP_201_CREATED)