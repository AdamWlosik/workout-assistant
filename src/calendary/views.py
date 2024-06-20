import calendar as cal
from datetime import datetime
from typing import TYPE_CHECKING

from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from calendary.forms import EventForm

from .models import Event

if TYPE_CHECKING:
    from django.http import HttpRequest, HttpResponse


@login_required
def calendar_view(request: "HttpRequest") -> "HttpResponse":
    today = datetime.today()  # noqa: DTZ002
    year = int(request.GET.get("year", today.year))
    month = int(request.GET.get("month", today.month))
    cal_obj = cal.Calendar(firstweekday=6)
    month_days = cal_obj.monthdayscalendar(year, month)

    events = []
    for week in month_days:
        week_events = [(day, Event.objects.filter(date__year=year, date__month=month)) for day in week]
        events.append(week_events)

    prev_month = (year, month - 1) if month > 1 else (year - 1, 12)
    next_month = (year, month + 1) if month < 12 else (year + 1, 1)  # noqa: PLR2004

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
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.user = request.user
            event.save()
            form.save_m2m()
            return redirect("calendary_view")
    else:
        form = EventForm()
    return render(request, "calendary/add_event.html", {"form": form})


@login_required
def event_detail(request: "HttpRequest", event_id: int) -> "HttpResponse":
    """Function tu display the details of a selected training"""
    event = get_object_or_404(Event, id=event_id, user=request.user)
    return render(request, "calendary/event_detail.html", {"event": event})
