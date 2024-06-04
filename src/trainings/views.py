from typing import TYPE_CHECKING  # noqa: I001

from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required

from .forms import TrainingForm
from .models import Trainings

if TYPE_CHECKING:
    from django.http import HttpResponse, HttpRequest  # noqa: I001

# TODO src/trainings/views.py:1:1: I001 [*] Import block is un-sorted or un-formatted
# src/trainings/views.py:10:1: I001 [*] Import block is un-sorted or un-formatted


@login_required
def trainings_list(request: HttpRequest) -> HttpResponse:
    trainings = Trainings.objects.filter(user=request.user)
    return render(request, "trainings/trainings_list.html", {"trainings": trainings})


@login_required
def training_detail(request: HttpRequest, training_id: int) -> HttpResponse:
    training = get_object_or_404(Trainings, id=training_id, user=request.user)
    return render(request, "trainings/training_detail.html", {"training": training})


@login_required
def training_create(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = TrainingForm(request.POST)
        if form.is_valid():
            training = form.save(commit=False)
            training.user = request.user
            form.save()
            return redirect("trainings")
    else:
        form = TrainingForm()
    return render(request, "trainings/training_form.html", {"form": form})


@login_required
def training_edit(request: HttpRequest, training_id: int) -> HttpResponse:
    training = get_object_or_404(Trainings, id=training_id, user=request.user)
    if request.method == "POST":
        form = TrainingForm(request.POST, instance=training)
        if form.is_valid():
            form.save()
            return redirect("trainings")
    else:
        form = TrainingForm(instance=training)
    return render(request, "trainings/training_form.html", {"form": form})


@login_required
def training_delete(request: HttpRequest, training_id: int) -> HttpResponse:
    training = get_object_or_404(Trainings, id=training_id, user=request.user)
    if request.method == "POST":
        training.delete()
        return redirect("trainings")
    return render(request, "trainings/training_confirm_delete.html", {"training": training})
