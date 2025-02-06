from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Measurement
from .forms import MeasurementForm

# Listar todos los registros
def measurement_list(request):
    measurements = Measurement.objects.all()
    return render(request, 'measurement_list.html', {'measurements': measurements})

# Crear un nuevo registro
def measurement_create(request):
    if request.method == "POST":
        form = MeasurementForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('measurement_list')
    else:
        form = MeasurementForm()
    return render(request, 'measurement_form.html', {'form': form})

# Editar un registro existente
def measurement_update(request, id):
    measurement = get_object_or_404(Measurement, id=id)
    if request.method == "POST":
        form = MeasurementForm(request.POST, instance=measurement)
        if form.is_valid():
            form.save()
            return redirect('measurement_list')
    else:
        form = MeasurementForm(instance=measurement)
    return render(request, 'measurement_form.html', {'form': form})

# Eliminar un registro
def measurement_delete(request, id):
    measurement = get_object_or_404(Measurement, id=id)
    if request.method == "POST":
        measurement.delete()
        return redirect('measurement_list')
    return render(request, 'measurement_confirm_delete.html', {'measurement': measurement})
