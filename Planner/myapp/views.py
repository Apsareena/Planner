from django.shortcuts import render, redirect
from django.http import HttpResponse
from myapp.forms import UserSignupForm, DiaryForm, TodoForm
from django.contrib.auth.decorators import login_required
from myapp.models import Todo, Diary
from django.utils import timezone
from django.utils.datastructures import MultiValueDictKeyError
# Create your views here.
def signup(request):
	if request.method=="POST":
		form = UserSignupForm(request.POST)
		if form.is_valid():
			form.save()
			# return HttpResponse('<script>alert("User Data Inserted successfully")</script>')
			return redirect('home')
	form = UserSignupForm()
	return render(request, 'myapp/signup.html', {'form':form})

def home(request):
	return render(request, 'myapp/home.html', {})


# @login_required
def todo(request):
	
	
	current_date = timezone.now()
	# content = request.POST['content']
	content = request.POST.get('content',False)
	created_obj = Todo.objects.create(added_date = current_date, task=content, user_id = request.user.id)
	length_of_todos = Todo.objects.all().count()
	Todo.objects.all().order_by('-added_date')
	Todo.objects.filter(task='False').delete()
	todo_items = Todo.objects.filter(user_id = request.user.id)
	return render(request, 'myapp/todo.html', {'todo_items':todo_items})

	


def delete_todo(request, todo_id):
	
	Todo.objects.filter(id=todo_id).delete()
	todo_items = Todo.objects.all().order_by('-added_date')
	return render(request, 'myapp/todo.html', {'todo_items':todo_items})


def diaryhome(request):
	Diary.objects.order_by('-date_posted')
	entry = Diary.objects.filter(user_id = request.user.id)
	return render(request, 'myapp/diaryhome.html', {'entry':entry})

def diary(request):
	
	current_date = timezone.now()
	context = request.POST.get('context', False)
	created_obj = Diary.objects.create(date_posted = current_date, diary=context, user_id = request.user.id)
	Diary.objects.filter(diary='False').delete()
	Diary.objects.all().order_by('-date_posted')
	form = Diary.objects.filter(user_id = request.user.id)
	return render(request, 'myapp/diary.html', {'form':form})

def header(request):
	return render(request, 'myapp/header.html')


def update_todo(request, todo_id):
	Todo.objects.filter(id=todo_id).delete()
	todo_items = Todo.objects.all().order_by('-added_date')

	return render(request, 'myapp/todo.html', {'todo_items': todo_items})


def lik(request):
	return render(request, 'myapp/lik.html')