from django import forms
from allauth.account.forms import SignupForm
from allauth.account.adapter import get_adapter

class CustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    mobile = forms.CharField(max_length=15)

    def save(self, request):
        adapter = get_adapter(request)
        user = adapter.new_user(request)
        user = adapter.save_user(request, user, self, commit=False)
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.username = self.cleaned_data["email"].split("@")[0]
        user.mobile = self.cleaned_data["mobile"]
        user.save()
        return user