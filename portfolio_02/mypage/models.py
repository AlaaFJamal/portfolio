from django.db import models

# Create your models here.
class Section(models.Model):
	name = models.CharField(max_length=20)
	description = models.CharField(max_length=30)
	content = models.TextField()
	pic = models.ImageField(null=True, blank=True)

	def __str__(self):
		return self.name