from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from .models import *
from .forms import *
from django.shortcuts import get_object_or_404
# Create your views here.
def home(request):
    banners = Banner.objects.filter(is_active=True)
    services = Service.objects.filter(is_active=True)
    meta = AgencyMeta.objects.filter(page_name="home").first()
    cookie_consent = CookieConsentSetting.objects.first()
    projects = Project.objects.filter(is_featured=True)
    latest_blogs = Blog.objects.filter(is_featured=True)  # change count if needed

    context = {
        "banners": banners,
        "services": services,
        "meta": meta,
        "cookie_consent": cookie_consent,
        'projects': projects,
        'lead_form': LeadForm(),
        'latest_blogs': latest_blogs,

    }
    return render(request, 'home.html', context)


def contact(request):
    form = LeadForm(request.POST or None)
    meta = AgencyMeta.objects.filter(page_name="contact").first()

    if form.is_valid():
        # Save to DB (so it appears in admin panel)
        lead = form.save()

        # Prepare email content
        subject = "New Contact Form Submission"
        message = f"""
        You have a new message from your website contact form:

        Name: {lead.name}
        Email: {lead.email}
        Phone: {lead.phone}
        Service:{lead.service}
        Message:{lead.message}
        """
        from_email = settings.DEFAULT_FROM_EMAIL
        recipient_list = [settings.CONTACT_EMAIL]  # Set in settings.py

        # Send email
        send_mail(subject, message, from_email, recipient_list, fail_silently=False)

        messages.success(request, "Thank you! We'll get in touch.")
        return redirect('contact')

    return render(request, 'contact.html', {'form': form, 'meta': meta})


def project_list(request):
    projects = Project.objects.all().order_by('-date_completed')
    meta = AgencyMeta.objects.filter(page_name="project_list").first()
    return render(request, 'projectlist.html', {'projects': projects, 'meta': meta})

def project_detail(request, slug):
    project = get_object_or_404(Project, slug=slug)
    meta = AgencyMeta.objects.filter(page_name="project_detail").first()
    return render(request, 'projectdetail.html', {'project': project, 'meta': meta})

def blog_list(request):
    blogs = Blog.objects.all()
    meta = AgencyMeta.objects.filter(page_name="blog_list").first()
    return render(request, 'bloglist.html', {'blogs': blogs, 'meta': meta})

def blog_detail(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    meta = AgencyMeta.objects.filter(page_name="blog_detail").first()
    return render(request, 'blogdetail.html', {'blog': blog, 'meta': meta})

def service_list(request):
    services = Service.objects.filter(is_active=True)
    meta = AgencyMeta.objects.filter(page_name="service_list").first()
    return render(request, 'servicelist.html', {'services': services, 'meta': meta})

def service_detail(request, slug):
    service = get_object_or_404(Service, slug=slug)
    meta = AgencyMeta.objects.filter(page_name="service_detail").first()
    return render(request, 'servicedetail.html', {'service': service, 'meta': meta})
def about(request):
    meta = AgencyMeta.objects.filter(page_name="about").first()
    return render(request, 'about.html' ,{'meta': meta})
