from django.shortcuts import render
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'frontend/index.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['my_variable'] = 'Some Value'
    #     return context


class AboutView(TemplateView):
    template_name = 'frontend/about.html'