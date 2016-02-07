from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
class ResearchGrant(models.Model):
	title = models.CharField(max_length=200)
	text = models.TextField()
	eligibility = models.TextField()
	how_to_apply = models.TextField()
	link = models.CharField(max_length=200)
	def	__str__(self):							
		return	self.title

class TravelGrant(models.Model):
	title = models.CharField(max_length=200)
	text = models.TextField()
	eligibility = models.TextField()
	how_to_apply = models.TextField()
	link = models.CharField(max_length=200)
	def	__str__(self):						
		return	self.title
class ConferenceGrant(models.Model):
	title = models.CharField(max_length=200)
	text = models.TextField()
	eligibility = models.TextField()
	how_to_apply = models.TextField()
	link = models.CharField(max_length=200)
	def	__str__(self):							
		return	self.title
class Fellowship(models.Model):
	title = models.CharField(max_length=200)
	text = models.TextField()
	link = models.CharField(max_length=200)
	def	__str__(self):						
		return	self.title
class Scholarship(models.Model):
	title = models.CharField(max_length=200)
	text = models.TextField()
	link = models.CharField(max_length=200)
	def	__str__(self):						
		return	self.title
class Message(models.Model):
	Post = models.CharField(max_length=200)
	text = models.TextField()
	def	__str__(self):						
		return	self.Post
class Student(models.Model):
	name = models.CharField(max_length=200)
	age = models.CharField(max_length=5)
	institute = models.CharField(max_length=200)
	address = models.TextField()
	qualification = models.CharField(max_length=300)
	works = models.TextField()
	tag_line = models.CharField(max_length=200)
	is_leader = models.BooleanField(default=False)
	achievement1 = models.CharField(max_length=200)
	achievement2 = models.CharField(max_length=200)
	achievement3 = models.CharField(max_length=200)
	def	__str__(self):						
		return	self.name

class Project(models.Model):
	start_date = models.CharField(max_length=15)
	end_date = models.CharField(max_length=15) 
	topic = models.CharField(max_length=200)
	details = models.TextField()
	no_of_interns_required = models.IntegerField()
	role_qualification = models.TextField()
	def	__str__(self):						
		return	self.topic



class StudentRel(models.Model):
	auth = models.ForeignKey(User,unique=True)
	mine = models.ForeignKey(Student,unique=True)


class StudentProject(models.Model):
	student = models.ForeignKey(Student)
	project = models.ForeignKey(Project)



class LeaderProject(models.Model):
	student = models.ForeignKey(Student)
	project = models.ForeignKey(Project)


class LeaderResearch(models.Model):
	student = models.ForeignKey(Student)
	project = models.ForeignKey(Project,unique=True)


class Request(models.Model):
	project = models.ForeignKey(Project)
	student = models.ForeignKey(Student,unique=True)


class Notice(models.Model):
	auth = models.ForeignKey(User)
	message = models.CharField(max_length=200)
	date = models.DateTimeField(default = timezone.now())
	def __str__(self):
		return self.message

# Create your models here.
