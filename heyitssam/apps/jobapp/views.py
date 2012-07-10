# Create your views here.
from models import *
from django.views.generic import DetailView, TemplateView

class CompanyDetailView(DetailView):
    model = JobApp

class ContactView(DetailView):
    model=JobApp
    template_name="jobapp/contact.html"

class CVDetailView(DetailView):
    model = JobApp
    template_name = 'jobapp/cv.html'

class ResumeDetailView(DetailView):
    model = JobApp
    template_name = 'jobapp/resume.html'

overview = CompanyDetailView.as_view()
cv_view = CVDetailView.as_view()
resume_view = ResumeDetailView.as_view()
contact_view = ContactView.as_view()
