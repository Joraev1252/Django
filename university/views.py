from django.shortcuts import render
from django.views.generic import ListView, TemplateView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import *

class UniversityViews(ListView):
    model = FamousUniversitie
    template_name = 'news.html'

class AllNews(ListView):
    model = FamousUniversitie
    template_name = 'all_news.html'
    context_object_name = 'news_list'

class UpdateNews(UpdateView):
    model = FamousUniversitie
    template_name = 'update_news.html'
    fields = ['name', 'image', 'about', 'country']

class DeleteNews(DeleteView):
    model = FamousUniversitie
    template_name = 'delete_news.html'
    success_url = reverse_lazy('university:')
    context_object_name = 'new'


class UniversityDetail(DetailView):
    model = FamousUniversitie
    template_name = "detail-page.html"
    context_object_name = 'news'

class AddViews(CreateView):
    model = FamousUniversitie
    template_name = 'add-news.html'
    fields = ['name', 'image', 'about', 'country', 'author']

class Universities(TemplateView):
    template_name = 'main/universities.html'

class Mit(TemplateView):
    template_name = 'main/mit.html'

class Columbia(TemplateView):
    template_name = 'main/columbia.html'

class Harvard(TemplateView):
    template_name = 'main/harvard.html'

class Stanford(TemplateView):
    template_name = 'main/stanford.html'

class HomeViews(ListView):
    model = FamousUniversitie
    template_name = 'news.html'

class EducationViews(TemplateView):
    template_name = 'main/education.html'

