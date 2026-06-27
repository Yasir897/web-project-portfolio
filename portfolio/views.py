from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Profile, SkillCategory, Education, Project, ContactMessage


def home(request):
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        message_text = request.POST.get('message', '').strip()
        if name and email and message_text:
            ContactMessage.objects.create(name=name, email=email, message=message_text)
            messages.success(request, 'Your message was sent successfully! I will get back to you soon.')
        return redirect('home')

    profile = Profile.objects.first()
    skill_categories = SkillCategory.objects.prefetch_related('skills').all()
    education = Education.objects.all()
    projects = Project.objects.all()

    return render(request, 'home.html', {
        'profile': profile,
        'skill_categories': skill_categories,
        'education': education,
        'projects': projects,
    })
