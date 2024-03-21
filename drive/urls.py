from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='drive'),
    path('upload', views.upload, name='upload'),
    path('<str:file_id>/delete', views.delete, name='delete'),
    path('<str:file_id>/', views.preview, name='preview')
]
