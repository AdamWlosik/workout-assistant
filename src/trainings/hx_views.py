from pprint import pprint
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from exercises.models import Exercise
from trainings.forms import TrainingExerciseForm
from trainings.models import Training, TrainingExercise
from django.contrib.auth.decorators import login_required


@login_required
def hx_training_exercise_add(request: "HttpRequest", training_id: int) -> "HttpResponse":
    pprint(request.POST)  # For debugging purposes, prints the POST data
    # <QueryDict: {'exercise': ['1'], 'rjf§0': ['reps1'], 'reps': ['["reps1"]'], 'training_id': ['1']}>

    # Fetch the training object, ensuring it belongs to the logged-in user
    training = get_object_or_404(Training, id=training_id, user=request.user)

    if request.method == "POST":
        exercises_id = request.POST.get("exercise")
        reps = request.POST.get("rjf§0")
        print(exercises_id, reps)
        exercise = get_object_or_404(Exercise, id=exercises_id)
        relation = TrainingExercise(exercise=exercise, training=training, reps=reps)
        print(relation)
        # TODO zwroc html który zwaiera
        #  1. liste wszystich exercise dla tego training (pod training.exercises) razem z reps
        #  2. utworzyć tego html
        return render(request, "hx_training_exercise_list.html", {"training": training})
    else:
        # If the request is not POST, render the form with the current training instance
        form = TrainingExerciseForm(instance=training)

    # Render the template with the form
    return render(request, "trainings/hx_training_exercise_form.html", {"form": form, "training": training})
