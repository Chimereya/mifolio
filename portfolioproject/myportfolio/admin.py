from django.contrib import admin

from .models import Portfolio, About, Projects, Skill, Contact

# Register your models here.

admin.site.register(Portfolio)
admin.site.register(About)
admin.site.register(Projects)
admin.site.register(Skill)
admin.site.register(Contact)
