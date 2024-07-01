from rest_framework.generics import CreateAPIView
from .serializers import CustomUserSerializer


class BaseRegistrationUser(CreateAPIView):
    serializer_class = CustomUserSerializer
