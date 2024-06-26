from django.shortcuts import render
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'index.html'


class ContactView(TemplateView):
    template_name = 'contact.html'


class AboutView(TemplateView):
    template_name = 'about.html'


class DomainView(TemplateView):
    template_name = 'domain.html'


class HostingView(TemplateView):
    template_name = 'hosting.html'
