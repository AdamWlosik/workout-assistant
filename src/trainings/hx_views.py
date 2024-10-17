import ast

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from exercises.models import Exercise

from trainings.forms import TrainingExerciseForm
from trainings.models import Training, TrainingExercise


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
        reps = request.POST.get("reps")
        reps_list = ast.literal_eval(reps.strip())
        exercise = get_object_or_404(Exercise, id=exercises_id)
        relation = TrainingExercise(exercise=exercise, training=training, reps=reps_list)
        relation.save()
        # return render(request, "trainings/hx_training_exercise_list.html", {"training": training})
        response = HttpResponse("")
        response.headers["HX-Trigger"] = "reload_list"
        return response
    else:
        # If the request is not POST, render the form with the current training instance
        form = TrainingExerciseForm(instance=training)

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
