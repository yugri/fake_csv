from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views import generic

from data_generator.models import Schema


class SchemeCreate(generic.CreateView):
    model = Schema
    fields = ['name', 'column_separator', 'string_character']
    success_url = reverse_lazy('data_generator:index')


class IndexView(generic.ListView):
    template_name = 'data_generator/index.html'
    context_object_name = 'generated_schemes'

    def get_queryset(self):
        """Return data schemas list with actions"""
        return Schema.objects.order_by('-created')


class DetailView(generic.DetailView):
    model = Schema
    template_name = 'data_generator/detail.html'