from django.views.generic import TemplateView
from apps.user.mixin import LoginRequiredCustomMixin

class IndexPageView(LoginRequiredCustomMixin, TemplateView):
    template_name = "frontend/pages/index.html"
