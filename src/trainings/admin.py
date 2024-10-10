from django.contrib import admin

from trainings.models import Category, Training, TrainingExercise


class ExerciseInline(admin.TabularInline):
    model = Training.exercises.through
    extra = 0


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Training)
class TrainingAdmin(admin.ModelAdmin):
    inlines = [
        ExerciseInline,
    ]


@admin.register(TrainingExercise)
class TrainingExerciseAdmin(admin.ModelAdmin):
    pass
