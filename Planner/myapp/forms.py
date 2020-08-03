from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from myapp.models import Todo, Diary

class UserSignupForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'first_name', 'last_name', 'email']

class DiaryForm(ModelForm):
	class Meta:
		model = Diary
		fields = ['diary']

		def _init_(self, *args, **kwargs):
			
			self.fields['text'].widget.attrs.update({'class':'textarea', 'placeholder':'Whats on your mind'})


class TodoForm(ModelForm):
	class Meta:
		model = Todo
		fields = ['task', 'added_date']