from django.urls import path

from . import views

app_name = "data_generator"
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('schemes/<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('schemes/create', views.SchemaCreateView.as_view(), name='create_scheme'),
    path('schemes/<int:pk>/update/', views.SchemaUpdateView.as_view(), name='update_scheme'),
    path('schemes/<int:pk>/delete/', views.SchemaDeleteView.as_view(), name='delete_scheme'),
    path('schemes/<int:pk>/data-sets/', views.DatasetList.as_view(), name='dataset_list')
]