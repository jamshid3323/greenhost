from django.shortcuts import render
from django.views.generic import TemplateView
from .models import *


class HostingView(TemplateView):
    template_name = 'hosting.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['hosting'] = HostingModel.objects.all()
        data['opportunities'] = OpportunityModel.objects.all()
        return data
