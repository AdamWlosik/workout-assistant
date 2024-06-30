import calendar as cal
import datetime
from typing import TYPE_CHECKING

from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.timezone import now

from calendary.forms import EventForm

from .models import Event

if TYPE_CHECKING:
    from django.http import HttpRequest, HttpResponse

DECEMBER = 12
JANUARY = 1


@login_required
def calendar_view(request: "HttpRequest") -> "HttpResponse":
    today = now()
    # TODO DTZ002 `datetime.datetime.today()` used  today = datetime.today() na today = datetime.now()
    # DTZ005 `datetime.datetime.now()` called without a `tz` argument today = datetime.now() na today = now()
    year = int(request.GET.get("year", today.year))
    month = int(request.GET.get("month", today.month))
    cal_obj = cal.Calendar(firstweekday=6)
    month_days = cal_obj.monthdayscalendar(year, month)

    events = []
    for week in month_days:
        week_events = [(day, Event.objects.filter(date__year=year, date__month=month)) for day in week]
        events.append(week_events)
    # TODO (przyszła optymalizacja) day jako datetime object

    prev_month = (year, month - 1) if month > JANUARY else (year - 1, DECEMBER)
    next_month = (year, month + 1) if month < DECEMBER else (year + 1, JANUARY)

    return render(
        request,
        "calendary/calendary_view.html",
        {
            "events": events,
            "month_days": month_days,
            "year": year,
            "month": month,
            "prev_month": prev_month,
            "next_month": next_month,
            "today": today,
        },
    )


@login_required
def add_event(request: "HttpRequest") -> "HttpResponse":
    day_params = request.GET.get("day")
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.user = request.user
            event.save()
            form.save_m2m()
            return redirect("calendary_view")
    else:
        initial_data = {}
        if day_params:
            initial_data["date"] = datetime.datetime.strptime(day_params, "%Y-%m-%d").astimezone(datetime.timezone.utc)
            # initial_data["date"] = datetime.strptime(day_params, "%Y-%m-%d").date()
            #  TODO DTZ007 Naive datetime constructed using `datetime.datetime.strptime()` without %z
        form = EventForm(initial=initial_data)
    return render(request, "calendary/event_form.html", {"form": form})


@login_required
def event_detail(request: "HttpRequest", event_id: int) -> "HttpResponse":
    """Function tu display the details of a selected training"""
    event = get_object_or_404(Event, id=event_id, user=request.user)
    return render(request, "calendary/event_detail.html", {"event": event})


@login_required
def event_edit(request: "HttpRequest", event_id: int) -> "HttpResponse":
    """Function to display view to create a new event"""

    event = get_object_or_404(Event, id=event_id, user=request.user)
    if request.method == "POST":
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            form.save_m2m()
            return redirect("calendary_view")
    else:
        form = EventForm(instance=event)
    return render(request, "calendary/event_form.html", {"form": form})
