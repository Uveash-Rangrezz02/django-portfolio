# Register your models here.
from django.contrib import admin
from .models import About, Project, Skill, Contact, Experience

admin.site.register(About)
admin.site.register(Project)
admin.site.register(Skill)
admin.site.register(Contact)
@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('company', 'role', 'start_date', 'end_date')