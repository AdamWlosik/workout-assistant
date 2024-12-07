from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

from calendary.models import Event


class HomePageView(TemplateView):
    """Class to display home page view"""

    template_name = "dashboard/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context["training_amount"] = Event.objects.filter(user=self.request.user, is_done=True).count()
            context["exercise_amount"] = "TODO"  # to nie potrzebne
            context["exercises"] = "TODO"
        return context
