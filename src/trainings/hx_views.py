import ast
import json
from datetime import datetime, timedelta
from pprint import pprint

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpRequest, JsonResponse
from django.shortcuts import get_object_or_404, render

from calendary.models import Event
from exercises.models import Exercise

from trainings.forms import TrainingExerciseForm
from trainings.models import Training, TrainingExercise
from trainings.services import update_reps_history, update_reps


@login_required
def hx_training_exercise_list(request: "HttpRequest", training_id: int) -> "HttpResponse":
    training_exercises = TrainingExercise.objects.filter(training_id=training_id)
    return render(request, "trainings/hx_training_exercise_list.html", {"training_exercises": training_exercises})


@login_required
def hx_training_exercise_add(request: "HttpRequest", training_id: int) -> "HttpResponse":
    # Fetch the training object, ensuring it belongs to the logged-in user
    training = get_object_or_404(Training, id=training_id, user=request.user)

    if request.method == "POST":
        exercises_id = request.POST.get("exercise")
        reps_proposed = request.POST.get("reps_proposed")
        # reps_list = ast.literal_eval(reps_proposed.strip())
        reps_list = ast.literal_eval(reps_proposed.strip()) if reps_proposed else []
        exercise = get_object_or_404(Exercise, id=exercises_id, user=request.user)
        relation = TrainingExercise(exercise=exercise, training=training, reps_proposed=reps_list, reps=[], user=request.user)
        relation.save()
        print(relation.reps_proposed)
        # return render(request, "trainings/hx_training_exercise_list.html", {"training": training})
        response = HttpResponse("")

        response.headers["HX-Trigger"] = "reload_list"
        return response
    else:
        # If the request is not POST, render the form with the current training instance
        form = TrainingExerciseForm(instance=training, user=request.user)

    # Render the template with the form
    return render(request, "trainings/hx_training_exercise_form.html", {"form": form, "training": training})


@login_required
def hx_training_exercise_delete(request: "HttpRequest", relation_id: int, training_id: int) -> "HttpResponse":
    training = get_object_or_404(Training, id=training_id, user=request.user)
    relation = get_object_or_404(TrainingExercise, id=relation_id)
    if request.method == "POST":
        relation.delete()
        response = HttpResponse("")
        response.headers["HX-Trigger"] = "reload_list"
        return response
    return HttpResponse(status=405)


# @login_required
# def hx_training_exercise_rep_edit(request: "HttpRequest", relation_id: int, training_id: int,
#                                   rep_index: int) -> "HttpResponse":
#     print(f"{relation_id=} {training_id=} {rep_index=}")
#     context = {
#         "relation_id": relation_id,
#         "training_id": training_id,
#         "rep_index": rep_index,
#     }
#     if request.method == "GET":
#         return render(request, "trainings/hx_training_exercise_rep_edit.html", context=context)
#     elif request.method == "POST":
#         print(request.POST)
#         rep_edit = request.POST.get("rep_edit")
#         print(rep_edit)
#         training_exercise = get_object_or_404(TrainingExercise, id=relation_id)
#         training_exercise.reps[rep_index] = rep_edit
#         training_exercise.is_done = False
#         training_exercise.save()
#         print(training_exercise.reps)
#         return HttpResponse(rep_edit)

@login_required
def hx_training_exercise_rep_edit(request: "HttpRequest", relation_id: int, training_id: int,
                                  rep_index: int, event_id: int) -> "HttpResponse":
    """Edycja repsa """
    print(f"{relation_id=} {training_id=} {rep_index=}")
    event = get_object_or_404(Event, id=event_id)
    context = {
        "relation_id": relation_id,
        "training_id": training_id,
        "rep_index": rep_index,
        "event": event,
    }
    if request.method == "GET":
        return render(request, "trainings/hx_training_exercise_rep_edit.html", context=context)
    elif request.method == "POST":
        print(request.POST)
        rep_edit = request.POST.get("rep_edit")
        print(rep_edit)
        """aktualizacja repsa"""
        training_exercise = update_reps(relation_id, rep_index, rep_edit)
        """aktualizacja historii repsa"""
        training_exercise = update_reps_history(training_exercise, event)
        messages.success(request, "Exercise save")
        return HttpResponse(rep_edit)
        # TODO """przygotowanie histori do wyswietlenia"""


@login_required
def hx_training_exercise_rep_add(request: "HttpRequest", relation_id: int, training_id: int,) -> "HttpResponse":
    training_exercise = get_object_or_404(TrainingExercise, id=relation_id, training_id=training_id)

    if request.method == "POST":
        new_rep = "kg x reps"
        training_exercise.reps.append(new_rep)
        training_exercise.save()
        response = HttpResponse("")
        response.headers["HX-Trigger"] = "reload_list" # TODO zobaczyć training_edit.html <a class="btn btn-main" hx-get="{% url 'hx-training-exercise-add' training.id %}"hx-target="#hx-training-exercise-add">Add Exercise</a>
        return response

    return HttpResponse(status=400)


# TODO dokończ widok edycji treningu całego
@login_required
def hx_training_exercise_edit(request: "HttpRequest", relation_id: int, training_id: int) -> "HttpResponse":
    training = get_object_or_404(Training, id=training_id, user=request.user)
    relation = get_object_or_404(TrainingExercise, id=relation_id, training=training)

    if request.method == "GET":
        # TODO zwroc mu formularz tworzenia z uzupełnionymi values
        form = TrainingExerciseForm(instance=training)  # TODO przygotować initial (instance=training, initial=)
    elif request.method == "POST":
        # TODO if request.method == "GET"
        exercises_id = request.POST.get("exercise")
        reps = request.POST.get("reps")
        pprint(request.POST)
        reps_list = ast.literal_eval(reps.strip())

        exercise = get_object_or_404(Exercise, id=exercises_id)
        relation.exercise = exercise
        relation.reps = reps_list
        relation.save()

        response = HttpResponse("")
        response.headers["HX-Trigger"] = "reload_list"
        return response
    else:
        form = TrainingExerciseForm(instance=relation)

    return render(
        request, "trainings/hx_training_exercise_form.html", {"form": form, "training": training, "relation": relation}
    )
