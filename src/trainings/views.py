from typing import TYPE_CHECKING  # noqa: I001

from django.forms import modelformset_factory
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required

from .forms import TrainingForm, TrainingExerciseForm
from .models import Training, TrainingExercise

if TYPE_CHECKING:
    from django.http import HttpResponse, HttpRequest  # noqa: I001

# TODO src/trainings/views.py:1:1: I001 [*] Import block is un-sorted or un-formatted
# src/trainings/views.py:10:1: I001 [*] Import block is un-sorted or un-formatted


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
def training_create(request):  # noqa: ANN001 ANN201 # TODO (Adam) ruff poprawic
    """Function to display view to create a new training"""

    TrainingExerciseFormSet = modelformset_factory(TrainingExercise, form=TrainingExerciseForm, extra=1)  # noqa: N806
    # TODO (Adam) porawic

    if request.method == "POST":
        form = TrainingForm(request.POST, request=request)
        formset = TrainingExerciseFormSet(request.POST, queryset=TrainingExercise.objects.none())

        if form.is_valid() and formset.is_valid():
            training = form.save(commit=False)
            training.user = request.user
            training.save()

            for form in formset.cleaned_data:
                if form:
                    exercise = form["exercise"]
                    reps = form["reps"]
                    TrainingExercise.objects.create(training=training, exercise=exercise, reps=reps)

            return redirect("training")

    else:
        form = TrainingForm(request=request)
        formset = TrainingExerciseFormSet(queryset=TrainingExercise.objects.none())

    return render(request, "trainings/training_form.html", {"form": form, "formset": formset})


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