from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class clinicaltrial(models.Model):
	author = models.CharField(max_length = 300)
	title = models.CharField(max_length = 300)
	creationDate = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return "Title: " + self.title + " -- Author: " + self.author

#to serve as a transaction
class file(models.Model):
	clinicaltrial = models.ForeignKey(clinicaltrial, on_delete = models.CASCADE, blank=True, null=True)
	owner = models.ForeignKey(User, related_name="owner", on_delete = models.CASCADE, blank=True, null=True, unique = False)
	sender = models.ForeignKey(User, related_name="sender", on_delete = models.CASCADE, blank=True, null=True, unique = False)
	filename = models.CharField(max_length = 100)
	file_type = models.CharField(max_length = 100, blank=True, null = True) 
	data = models.FileField()
	uploadDate = models.DateTimeField(auto_now_add=True)
	dataHash = models.CharField(max_length = 100, blank = True, null= True)
	
	def __str__(self):
		return self.filename 

#or perhaps foreign key reference to self? duplicate file transaction model for each user upon creation?
#User has many files database model? put hash directly in file model? duplicate blocks for each user? 
#Perhaps each user has a pointer to one genesis block?
# parent = models.ForeignKey("self")



# #to encapsulate the transaction into a blockchain 
# class block(models.Model):
# 	fileReference = models.ForeignKey(file, on_delete = models.CASCADE, blank=True, null=True)
# 	index = models.IntegerField(blank=True, null = True)
# 	hashString = models.CharField(max_length = 500, blank=True, null = True)
# 	previousHash = models.CharField(max_length = 500, blank=True, null = True)















