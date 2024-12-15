import json
from datetime import datetime, timedelta

from django.shortcuts import get_object_or_404

from trainings.models import TrainingExercise


def update_reps(relation_id, rep_index, rep_edit):
    training_exercise = get_object_or_404(TrainingExercise, id=relation_id)
    training_exercise.reps[rep_index] = rep_edit
    training_exercise.is_done = False
    training_exercise.save()

    return training_exercise


def update_reps_history(training_exercise):
    print("Running history reps update", training_exercise.reps)
    reps = training_exercise.reps
    # current_date = datetime.now().strftime("%d.%m.%Y")
    current_date = (datetime.now() + timedelta(days=10)).strftime("%d.%m.%Y")
    history = json.loads(training_exercise.history)
    date_entry = next((entry for entry in history if entry["date"] == current_date), None)
    if date_entry:
        date_entry["reps"] = [reps]
    else:
        history.append({"date": current_date, "reps": [reps]})
    training_exercise.history = json.dumps(history)
    print(training_exercise.history)
    training_exercise.is_done = True
    training_exercise.save()
    return training_exercise