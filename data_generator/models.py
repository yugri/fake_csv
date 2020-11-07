from django.db import models

from fake_csv.settings import SEPARATOR_CHOICES, STRING_CHAR_CHOICES, DATA_TYPES


class Schema(models.Model):
    name = models.CharField(max_length=256)
    column_separator = models.CharField(max_length=5, default=',', choices=SEPARATOR_CHOICES)
    string_character = models.CharField(max_length=5, default='"', choices=STRING_CHAR_CHOICES)
    last_modified = models.DateTimeField(auto_now=True)
    created = models.DateField(auto_now_add=True)


class Column(models.Model):
    schema = models.ForeignKey(Schema, on_delete=models.CASCADE)
    name = models.CharField(max_length=256)
    type = models.CharField(max_length=64, choices=DATA_TYPES)
    order = models.IntegerField()