from django.urls import path
from myapp import views
from django.contrib.auth import views as auth_views

urlpatterns=[
	path('', views.home),
	path('signup/', views.signup, name='signup'),
	path('signin/', auth_views.LoginView.as_view(template_name='myapp/signin.html'), name='signin'),
	path('signout/', auth_views.LogoutView.as_view(template_name='myapp/signout.html'), name='signout'),
	path('todo/', views.todo, name='todo'),
	path('diaryhome/', views.diaryhome, name='diaryhome'),
	path('home/', views.home, name='home'),
	path('diary/', views.diary, name='diary'),
	path('delete_todo/<int:todo_id>/', views.delete_todo, name='delete_todo'),
	
	
	]