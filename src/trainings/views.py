from typing import TYPE_CHECKING

from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import TrainingForm
from .models import Training

if TYPE_CHECKING:
    from django.http import HttpRequest, HttpResponse


@login_required
def trainings_list(request: "HttpRequest") -> "HttpResponse":
    """Function tu display a list of trainings"""
    trainings = Training.objects.filter(user=request.user)
    return render(request, "trainings/trainings_list.html", {"trainings": trainings})


@login_required
def training_detail(request: "HttpRequest", training_id: int) -> "HttpResponse":
    """Function tu display the details of a selected training"""
    training = get_object_or_404(Training, id=training_id, user=request.user)
    return render(request, "trainings/training_detail.html", {"training": training})


@login_required
def training_create(request: "HttpRequest") -> "HttpResponse":
    """Function to display view to create a new training"""

    if request.method == "POST":
        form = TrainingForm(request.POST, request=request)
        if form.is_valid():
            training = form.save(commit=False)
            training.user = request.user
            form.save()
            form.save_m2m()
            return redirect("trainings")
    else:
        form = TrainingForm(request=request)

    return render(request, "trainings/training_form.html", {"form": form})


@login_required
def training_edit(request: "HttpRequest", training_id: int) -> "HttpResponse":
    """Function to display view to create a new training"""

    training = get_object_or_404(Training, id=training_id, user=request.user)
    if request.method == "POST":
        form = TrainingForm(request.POST, instance=training, request=request)
        if form.is_valid():
            form.save()
            form.save_m2m()
            return redirect("trainings")
    else:
        form = TrainingForm(instance=training, request=request)
    return render(request, "trainings/training_form.html", {"form": form})


@login_required
def training_delete(request: "HttpRequest", training_id: int) -> "HttpResponse":
    """Function to display view to delete an existing training"""
    training = get_object_or_404(Training, id=training_id, user=request.user)
    if request.method == "POST":
        training.delete()
        return redirect("trainings")
    return render(request, "trainings/training_confirm_delete.html", {"training": training})
