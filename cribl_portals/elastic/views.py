from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import AddClusterForm
from .models import ElasticDestination, ElasticDestinationUpdate

def destination_home(request):
    if request.user.is_authenticated:
        destinations = ElasticDestination.objects.all()
        return render(request, 'destination_home.html', {"destinations": destinations})
    else:
        messages.success(request, "You must be logged in to view that page...")
        return redirect("login")
    
def destination_get(request, pk):
    if request.user.is_authenticated:
        destination = ElasticDestination.objects.get(id=pk)
        return render(request, 'destination.html', {"destination": destination})
    else:
        messages.success(request, "You must be logged in to view that page...")
        return redirect("login")

def destination_status(request, pk, status):
    if request.user.is_authenticated:
        destination = ElasticDestination.objects.get(id=pk)
        if destination.status != status:
            destination.status = status
            destination.message = f" Status changed to {destination.get_status_display()}"
            destination.save()
            messages.success(request, f"Destination  has been {'enabled' if destination.status == 0 else 'disabled'}...")
        return redirect("elastic_home")
    else:
        messages.success(request, "You must be logged in to view that page...")
        return redirect("login")

def destination_delete(request, pk):
    if request.user.is_authenticated:
        destination = ElasticDestination.objects.get(id=pk)
        destination.delete()
        messages.success(request, "Destination deleted successfully...")
        return redirect("elastic_home")
    else:
        messages.success(request, "You must be logged in to view that page...")
        return redirect("login")

def destination_add(request):
    form = AddClusterForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_record = form.save()
                messages.success(request, "Destination added...")
                return redirect("elastic_home")
        return render(request, 'destination_add.html', {"form": form})
    else:
        messages.success(request, "You must be logged in to view that page...")
        return redirect("login")

def destination_update(request, pk):
    if request.user.is_authenticated:
        destination = ElasticDestination.objects.get(id=pk)
        destination.message = "Record has been updated"
        form = AddClusterForm(request.POST or None, instance=destination)
        if form.is_valid():
            form.save()
            messages.success(request, "Destination has been updated...")
            return redirect("elastic_home")
        return render(request, 'destination_update.html', {"form": form, "destination_id": pk})
    else:
        messages.success(request, "You must be logged in to view that page...")
        return redirect("login")