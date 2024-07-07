from django.shortcuts import render, reverse
from django.views.generic import TemplateView, CreateView
from main.forms import MessageForm
from main.models import TeamMember, MessageModel
from hostings.models import HostingModel
from django.core.mail import send_mail
from django.conf.global_settings import EMAIL_HOST_USER
from .utils import send_bot_message


class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['members'] = TeamMember.objects.all()
        data['hosting'] = HostingModel.objects.all()
        return data


class ContactView(CreateView):
    model = MessageModel
    form_class = MessageForm
    template_name = 'contact.html'

    def get_success_url(self):
        return reverse('main:home')

    def form_invalid(self, form):
        return super().form_invalid(form)

    def form_valid(self, form):
        # message = f"Assalomu alaykum {form.instance.name}! xabaringizni qabul qildim."
        # send_mail("Yangi xabar", message, EMAIL_HOST_USER, [form.instance.email])
        send_bot_message(form.cleaned_data)
        return super().form_valid(form)


class AboutView(TemplateView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['members'] = TeamMember.objects.all()
        return data


class DomainView(TemplateView):
    template_name = 'domain.html'
