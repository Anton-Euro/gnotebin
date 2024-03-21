from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.index, name='pin_create'),
    path('<slug:pin_id>/', views.preview, name='pin_preview'),
    path('<slug:pin_id>/download', views.download, name='pin_download'),
    path('<slug:pin_id>/delete', views.delete, name='pin_delete')
]