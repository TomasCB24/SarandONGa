from django.urls import path
from . import views

urlpatterns = [
    path('create',views.proyect_create, name='proyect_create'),
    path('<int:proyect_id>/delete',
        views.proyect_delete, name="proyect_delete"),
    path('<int:proyect_id>/update', views.proyect_update, name='proyect_update')
]