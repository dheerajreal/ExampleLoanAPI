from django.contrib.auth import get_user_model
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .permissions import AdminPermission, AgentPermission
from .serializers import UserSerializer, UserUpdateSerializer

User = get_user_model()


class UsersListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, AdminPermission | AgentPermission]


class UsersRUView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserUpdateSerializer
    permission_classes = [IsAuthenticated, AdminPermission | AgentPermission]
