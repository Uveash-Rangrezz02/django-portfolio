# Create your models here.
from django.db import models

from django.db import models

class About(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    experience = models.PositiveIntegerField()
    projects = models.PositiveIntegerField()

    def __str__(self):
        return self.title


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    tech_stack = models.CharField(max_length=200)
    github_link = models.URLField(blank=True)
    live_link = models.URLField(blank=True)
    image = models.ImageField(upload_to='projects/')

    def __str__(self):
        return self.title

# core/models.py
class Skill(models.Model):
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name



class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Experience(models.Model):
    company = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    start_date = models.CharField(max_length=50)
    end_date = models.CharField(max_length=50)
    location = models.CharField(max_length=100, blank=True)
    description = models.TextField()

    def __str__(self):
        return self.company
