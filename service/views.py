from django.shortcuts import render, get_object_or_404, redirect
from .forms import CreateNewService
from .models import Service
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from main.views import asem_required


@login_required
@asem_required
def service_create(request):
    if request.method == "POST":
        form = CreateNewService(request.POST)
        if form.is_valid():
            form.save()
            return redirect('service_list')

    form = CreateNewService()
    return render(request, 'service/service_form_backend.html', {"form": form, "title": "Crear Servicio", 'page_title': 'SarandONGa 💃 - Crear Servicio'})


@login_required
@asem_required
def service_list(request):

    context = {
        'objects': Service.objects.all(),
        'objects_json': '[]',
        'object_name': 'Servicio',
        'object_name_en': 'service',
        'title': 'Gestión de servicios',
        'page_title': 'SarandONGa 💃 - Gestión de Servicios'
    }

    return render(request, 'service_list.html', context)

@login_required
@asem_required
def service_update(request, service_id):
    service = get_object_or_404(Service, id=service_id)
    if request.method == "POST":
        form = CreateNewService(request.POST, request.FILES,instance=service)
        if form.is_valid():
            form.save()
            return redirect('service_list')
        else:
            messages.error(request, 'Formulario con errores')
    else: 
        form = CreateNewService(instance=service)
    return render(request, 'service/service_form_backend.html', {"form": form, "title": "Editar Servicio", 'page_title': 'SarandONGa 💃 - Editar Servicio'})

@login_required
@asem_required
def service_delete(request, service_id):
    service = get_object_or_404(Service, id=service_id)
    service.delete()
    return redirect('service_list')

@login_required
@asem_required  #TODO
def service_details(request, service_id):
    service = get_object_or_404(Service, id=service_id)
    return render(request, 'service/service_details.html', {'service': service})

