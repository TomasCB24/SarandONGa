from django.urls import path
from . import views

urlpatterns = [
    path("list",views.sponsorship_list,name="sponsorship_list"),
    path("create",views.sponsorship_create,name="sponsorship_create"),
    path("delete",views.sponsorship_delete, name="sponsorship_delete")
] 