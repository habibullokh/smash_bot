from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
)
from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
# from .permissions import IsOwner, IsAdmin
from .serialezers import UserSerializers
from .models import User


class UsersAPIViews(ListAPIView):
    """
    get:
        Returns the detail of a products category

        parameters: [id, telegram_id, user_name]

    """
    queryset = User.objects.all()
    serializer_class = UserSerializers
    permission_classes = [AllowAny]


