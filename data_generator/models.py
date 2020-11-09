from django.db import models
from django.urls import reverse

from fake_csv.settings import SEPARATOR_CHOICES, STRING_CHAR_CHOICES, DATA_TYPES


class Schema(models.Model):
    name = models.CharField(max_length=256)
    column_separator = models.CharField(max_length=5, default=',', choices=SEPARATOR_CHOICES)
    string_character = models.CharField(max_length=5, default='"', choices=STRING_CHAR_CHOICES)
    last_modified = models.DateTimeField(auto_now=True)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("data_generator:detail", kwargs={"id", self.id})


class Column(models.Model):
    schema = models.ForeignKey(Schema, on_delete=models.CASCADE)
    name = models.CharField(max_length=256)
    column_type = models.CharField(max_length=64, choices=DATA_TYPES)
    order = models.IntegerField()

    def __str__(self):
        return self.name


class Dataset(models.Model):
    schema = models.ForeignKey(Schema, on_delete=models.CASCADE)
    status = models.BooleanField(blank=True, null=True)
    created = models.DateField(auto_now_add=True)
    upload = models.FileField(upload_to='media/')

    def __str__(self):
        return "Dataset for {0}, created at {1}".format(self.schema.name, self.created)
