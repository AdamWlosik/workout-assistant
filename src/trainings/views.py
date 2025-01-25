from typing import TYPE_CHECKING

from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import TrainingExerciseFormSet, TrainingForm
from .models import Training

if TYPE_CHECKING:
    from django.http import HttpRequest, HttpResponse


@login_required
def trainings_list(request: "HttpRequest") -> "HttpResponse":
    trainings = Training.objects.filter(user=request.user, is_copy=False)
    return render(request, "trainings/trainings_list.html", {"trainings": trainings})


@login_required
def training_detail(request: "HttpRequest", training_id: int) -> "HttpResponse":
    training = get_object_or_404(Training, id=training_id, user=request.user)
    return render(request, "trainings/training_detail.html", {"training": training})


@login_required
def training_create(request: "HttpRequest") -> "HttpResponse":
    if request.method == "POST":
        form = TrainingForm(request.POST, request=request, formset_data=request.POST)
        formset = TrainingExerciseFormSet(request.POST, instance=Training())
        if form.is_valid():
            training = form.save(commit=False)
            training.user = request.user
            training.save()
            form.save_m2m()
            formset.instance = training
            formset.save()
            return redirect("trainings")
    else:
        form = TrainingForm(request=request)
        formset = TrainingExerciseFormSet(instance=Training())

    return render(request, "trainings/training_form.html", {"form": form, "formset": formset})


@login_required
def training_edit(request: "HttpRequest", training_id: int) -> "HttpResponse":
    training = get_object_or_404(Training, id=training_id, user=request.user)
    if request.method == "POST":
        form = TrainingForm(request.POST, instance=training, request=request)
        if form.is_valid():
            form.save()
            return redirect("trainings")
    else:
        form = TrainingForm(instance=training, request=request)

    return render(request, "trainings/training_edit.html", {"form": form, "training": training})


@login_required
def training_delete(request: "HttpRequest", training_id: int) -> "HttpResponse":
    training = get_object_or_404(Training, id=training_id, user=request.user)
    if request.method == "POST":
        training.delete()
        return redirect("trainings")
    return render(request, "trainings/training_confirm_delete.html", {"training": training})
