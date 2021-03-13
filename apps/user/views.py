from allauth.account.views import PasswordChangeView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

class CustomPasswordChangeView(PasswordChangeView):
    def get_success_url(self):
        return reverse_lazy('account_login')


customPasswordChanged = login_required(CustomPasswordChangeView.as_view())