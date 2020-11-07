from django.urls import path

from . import views

app_name = "data_generator"
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('schemes/<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('schemes/create', views.SchemeCreate.as_view(), name='create_scheme')
]