# backends.py
from django.contrib.auth.backends import ModelBackend
from .models import User

from django.db.models import Q

class CustomUserBackend(ModelBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        return User.objects.filter(Q(password=password) and Q(email=email)).first()
         

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
