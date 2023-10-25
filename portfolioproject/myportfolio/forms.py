from django import forms
from .models import Portfolio, About, Projects, Skill, Contact
from django.forms import ModelForm


class PostForm(ModelForm):
    class Meta:
        model = Portfolio
        fields = ['name', 'short_bio']


class AboutForm(ModelForm):
    class Meta:
        model = About
        fields = ['image', 'bio']
        
class SkillForm(ModelForm):
    class Meta:
        model = Skill
        fields = ['skill_name']
        
        
class ProjectForm(ModelForm):
    class Meta:
        model = Projects
        fields = '__all__'

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'