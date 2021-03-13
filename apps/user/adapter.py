from allauth.account.adapter import DefaultAccountAdapter
from hermes_tradebot.settings import IS_OPEN_FOR_SIGN_UP

class CustomAccountAdapter(DefaultAccountAdapter):
    def is_open_for_signup(self, request):
        return IS_OPEN_FOR_SIGN_UP