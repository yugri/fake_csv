from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views import generic

from data_generator.forms import SchemaModelForm
from data_generator.models import Schema, Dataset, Column


class SchemaCreateView(generic.CreateView):
    template_name = "data_generator/schema_form.html"
    form_class = SchemaModelForm
    # model = Schema
    # fields = ['name', 'column_separator', 'string_character']
    success_url = reverse_lazy('data_generator:index')


class SchemaUpdateView(generic.UpdateView):
    template_name = "data_generator/schema_update_form.html"
    form_class = SchemaModelForm
    success_url = reverse_lazy('data_generator:index')

    def get_object(self):
        return get_object_or_404(Schema, id=self.kwargs.get("pk"))

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the columns
        context['columns'] = Column.objects.filter(schema=self.kwargs.get("pk"))
        return context


class SchemaDeleteView(generic.DeleteView):
    model = Schema
    success_url = reverse_lazy('data_generator:index')


class IndexView(generic.ListView):
    template_name = 'data_generator/index.html'
    context_object_name = 'schemes'
    queryset = Schema.objects.order_by('-created')
    #
    # def get_queryset(self):
    #     """Return data schemas list with actions"""
    #     return Schema.objects.order_by('-created')


class DetailView(generic.DetailView):
    model = Schema
    template_name = 'data_generator/detail.html'


class DatasetList(generic.ListView):
    template_name = 'data_generator/dataset_list.html'
    context_object_name = "datasets"

    def get_queryset(self):
        """Return all datasets under requested scheme"""
        return Dataset.objects.order_by('-created')
