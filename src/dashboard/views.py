from django.views.generic import TemplateView


class HomePageView(TemplateView):
    """Class to display home page view"""

    template_name = "home.html"
