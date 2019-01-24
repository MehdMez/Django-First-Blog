from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
	author = models.ForeignKey('auth.User', on_delete=models.CASCADE) #models.CASCADE ->
	title = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(blank=True, null=True) #Peut être vide et/ou null

	def publish(self):
		self.published_date=timezone.now()   #Date de publication = maitenant
		self.save()

	def __str__(self):
		return self.title