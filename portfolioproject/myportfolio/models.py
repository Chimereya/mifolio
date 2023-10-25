from django.db import models

# Create your


class Portfolio(models.Model):
    name = models.CharField(max_length=100)
    short_bio = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class About(models.Model):
    image = models.ImageField(upload_to='static/images', blank=True, null=True)
    bio = models.TextField()

    def __str__(self):
        return self.bio
    
    
class Skill(models.Model):
    
    skill_name = models.CharField(max_length=80)

    def __str__(self):
        return self.skill_name


class Projects(models.Model):
    project_image = models.ImageField(upload_to='static/images', blank=True, null=True)
    project_name = models.CharField(max_length=200)
    about_project = models.TextField()
    view_project = models.URLField(null=True)

    def __str__(self):
        return self.project_name

class Contact(models.Model):
    email = models.URLField(null=True)
    github = models.URLField(null=True)
    linkedin = models.URLField(null=True)
    twitter = models.URLField(null=True)

    def __str__(self):
        return 'contacts'

