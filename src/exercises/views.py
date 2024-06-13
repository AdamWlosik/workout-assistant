from typing import TYPE_CHECKING  # noqa: I001

from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required

from .forms import ExerciseForm
from .models import Exercise

if TYPE_CHECKING:
    from django.http import HttpResponse, HttpRequest  # noqa: I001


@login_required
def exercises_list(request: "HttpRequest") -> "HttpResponse":
    """Function tu display a list of exercises"""
    exercises = Exercise.objects.filter(user=request.user)
    return render(request, "exercises/exercises_list.html", {"exercises": exercises})


@login_required
def exercise_detail(request: "HttpRequest", exercise_id: int) -> "HttpResponse":
    """Function tu display the details of a selected exercise"""
    exercise = get_object_or_404(Exercise, id=exercise_id, user=request.user)
    return render(request, "exercises/exercise_detail.html", {"exercise": exercise})


@login_required
def exercise_create(request: "HttpRequest") -> "HttpResponse":
    """Function to display view to create a new exercise"""
    if request.method == "POST":
        form = ExerciseForm(request.POST)
        if form.is_valid():
            exercise = form.save(commit=False)
            exercise.user = request.user
            form.save()
            return redirect("exercises")
    else:
        form = ExerciseForm()
    return render(request, "exercises/exercise_form.html", {"form": form})


@login_required
def exercise_edit(request: "HttpRequest", exercise_id: int) -> "HttpResponse":
    """Function to display view to create a new exercise"""
    exercise = get_object_or_404(Exercise, id=exercise_id, user=request.user)
    if request.method == "POST":
        form = ExerciseForm(request.POST, instance=exercise)
        if form.is_valid():
            form.save()
            return redirect("exercises")
    else:
        form = ExerciseForm(instance=exercise)
    return render(request, "exercises/exercise_form.html", {"form": form})


@login_required
def exercise_delete(request: "HttpRequest", exercise_id: int) -> "HttpResponse":
    """Function to display view to delete an existing exercise"""
    exercise = get_object_or_404(Exercise, id=exercise_id, user=request.user)
    if request.method == "POST":
        exercise.delete()
        return redirect("exercises")
    return render(request, "exercises/exercise_confirm_delete.html", {"exercise": exercise})
