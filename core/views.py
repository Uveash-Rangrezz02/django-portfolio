from django.shortcuts import render
from .models import About, Skill, Project, Experience

def home(request):
    about = About.objects.order_by('-id').first()
    skills = Skill.objects.all().order_by('id')
    projects = Project.objects.all().order_by('-id')
    experiences = Experience.objects.all().order_by('-id')

    context = {
        'about': about,
        'skills': skills,
        'projects': projects,
        'experiences': experiences,
    }

    return render(request, 'core/home.html', context)

from django.shortcuts import render
from .models import About, Skill, Project, Experience


def home(request):
    about = About.objects.order_by('-id').first()
    skills = Skill.objects.all().order_by('id')
    projects = Project.objects.all().order_by('-id')
    experiences = Experience.objects.all().order_by('-id')

    context = {
        'about': about,
        'skills': skills,
        'projects': projects,
        'experiences': experiences,
    }

    return render(request, 'core/home.html', context)


def contact(request):   # ✅ THIS FUNCTION MUST EXIST
    return render(request, "core/contact.html")

from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

def contact(request):
    if request.method == "POST":
        email = request.POST.get("email")
        message = request.POST.get("message")

        send_mail(
            subject=f"New Contact Message from {email}",
            message=message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=["rangrezzuveash@gmail.com"],  # tumhara email
        )

        return render(request, "core/contact.html", {
            "success": True
        })

    return render(request, "core/contact.html")
