from django.shortcuts import render, redirect
from .models import Todo


# Create your views here.


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
            return redirect('/')
        else:
            pass
    
    context={
        'todos':todo,
    }

    return render(request, 'index.html', context)

def delete(request, pk):
    todo=Todo.objects.get(id=pk)
    todo.delete()
    return redirect('/')