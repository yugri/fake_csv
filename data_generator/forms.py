from django import forms

from data_generator.models import Schema


class SchemaModelForm(forms.ModelForm):
    """Handle our scheme parameters"""
    class Meta:
        model = Schema
        fields = ['name', 'column_separator', 'string_character']