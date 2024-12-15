import json
from datetime import datetime, timedelta
from time import sleep
from typing import TYPE_CHECKING, List, Dict

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from calendary.models import Event
from .forms import TrainingExerciseFormSet, TrainingForm
from .models import Training, TrainingExercise

if TYPE_CHECKING:
    from django.http import HttpRequest, HttpResponse


@login_required
def trainings_list(request: "HttpRequest") -> "HttpResponse":
    trainings = Training.objects.filter(user=request.user)
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


# @login_required
# def mark_done_exercise(request: "HttpRequest", training_exercise_id: int, event_id: int) -> "HttpResponse":
#     if request.method == "POST":
#         training_exercise = get_object_or_404(TrainingExercise, id=training_exercise_id, user=request.user)
#         print(training_exercise.id)
#         print(training_exercise.is_done)
#         print(training_exercise.reps)
#         reps = training_exercise.reps
#         if not training_exercise.is_done:
#             # current_date = datetime.now().strftime("%d.%m.%Y")
#             current_date = (datetime.now() + timedelta(days=9)).strftime("%d.%m.%Y")
#             history = json.loads(training_exercise.history)
#             date_entry = next((entry for entry in history if entry["date"] == current_date), None)
#             if date_entry:
#                 date_entry["reps"] = reps
#             else:
#                 history.append({"date": current_date, "reps": [reps]})
#             training_exercise.history = json.dumps(history)
#             print(training_exercise.history)
#             training_exercise.is_done = True
#             messages.success(request, "Exercise save")
#             training_exercise.save()
#
#     return redirect("event_detail", event_id=event_id)


@login_required
def display_history(request: "HttpRequest", training_exercise_id: int, event_id: int) -> "HttpResponse":
    if request.method == "POST":
        training_exercise = get_object_or_404(TrainingExercise, id=training_exercise_id, user=request.user)
        event = get_object_or_404(Event, id=event_id, user=request.user)
        history = json.loads(training_exercise.history)
        display_history = [
            {
                "date": entry["date"],
                "reps": entry["reps"]
            }
            for entry in history[-4:]
        ]
        print(display_history)
        return render(request, "calendary/event_detail.html", {
            "event": event,
            "training_exercise_history": display_history,
            "current_training_exercise_id": training_exercise_id,
        })

    return redirect("event_detail", event_id=event_id)


