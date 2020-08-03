from django.db import models
from django.contrib.auth.models import User

# class Planner(models.Model):
# 	# date_posted = models.DateTimeField(auto_now_add=True)
# 	added_date = models.DateTimeField()
# 	task = models.CharField(max_length=200)
# 	# diary = models.TextField()
# 	# notes = models.CharField(max_length=400)
# 	user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

# 	def __str__(self):
# 		return 'Entry #{}'.format(self.id)

# 	class Meta:
# 		verbose_name_plural = 'entry'

class Diary(models.Model):
	diary = models.TextField()
	date_posted = models.DateTimeField(auto_now_add=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

	def __str__(self):
		return 'Entry #{}'.format(self.user_id)

	class Meta:
		verbose_name_plural = 'entry'

class Todo(models.Model):
	added_date = models.DateTimeField()
	task = models.CharField(max_length=200, null=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE, null = True)

	def __str__(self):
		return 'Task #{}'.format(self.user_id)
