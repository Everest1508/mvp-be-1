from rest_framework.permissions import BasePermission
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
import jwt
from django.conf import settings
from .models import User

class IsJWTAuthenticated(BaseAuthentication):
    def authenticate(self, request):
        token = request.headers.get('Authorization').split()[1]
        if not token:
            return None
        try:
            decoded_data = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Token has expired')
        except jwt.InvalidTokenError:
            raise AuthenticationFailed('Invalid token')
        
        user_id = decoded_data.get('id')
        if user_id is None:
            return None
        
        # token=request.headers.get('Authorization')
        # decoded_data = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
        print(decoded_data)
        try:
            user = User.objects.get(id=decoded_data["id"])
            # user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return None

        return user, None

