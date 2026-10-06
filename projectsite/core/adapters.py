from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from allauth.socialaccount.models import SocialAccount
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomSocialAccountAdapter(DefaultSocialAccountAdapter):
    def is_auto_signup_allowed(self, request, sociallogin):
        return True

    def populate_user(self, request, sociallogin, data):
        user = super().populate_user(request, sociallogin, data)
        # Auto-generate username from email if not provided by Google
        if not user.username and user.email:
            user.username = user.email.split('@')[0]
        return user

    def pre_social_login(self, request, sociallogin):
        # Auto-connect social account if local account with same email already exists
        if sociallogin.is_existing:
            return

        if not sociallogin.email_addresses:
            return

        email = sociallogin.email_addresses[0].email
        try:
            user = User.objects.get(email=email)
            sociallogin.connect(request, user)
        except User.DoesNotExist:
            pass