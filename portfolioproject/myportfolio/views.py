from django.shortcuts import render
from .models import Portfolio, About, Projects, Skill, Contact
from .forms import PostForm, AboutForm, ProjectForm, SkillForm


# Create your views here.


def portfolio(request):
    about = About.objects.all().first()
    port = Portfolio.objects.all().first()
    all_skills = Skill.objects.all()
    all_projects = Projects.objects.all()
    all_contacts = Contact.objects.all().first
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

    else:
        form = PostForm()
    return render(request, 'myportfolio/portfolio.html', {'port': port, 'about': about,
                                                          'form': form, 'all_skills': all_skills,
                                                          'all_projects': all_projects,
                                                          'all_contacts': all_contacts})


def about_me(request):
    about = About.objects.all().first()
    all_skills = Skill.objects.all()
    if request.method == 'POST':
        form = AboutForm(request.POST)
        form = SkillForm(request.POST)
        if form.is_valid():
            form.save()

    else:
        form = AboutForm()
        form = SkillForm()
    return render(request, 'myportfolio/portfolio.html', {'about': about,
                                                          'all_skills': all_skills,
                                                          'form': form})


def my_projects(request):
    all_projects = Projects.objects.all()
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

    else:
        form = ProjectForm()
    return render(request, 'myportfolio/portfolio.html', {'all_projects': all_projects,
                                                          'form': form})


def contacts(request):
    all_contacts = Contact.objects.all().first
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()

    else:
        form = ContactForm()
    return render(request, 'myportfolio/portfolio.html', {'all_contacts': all_contacts,
                                                          'form': form})