from django.contrib.auth import get_user_model
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .permissions import AdminPermission, AgentPermission
from .serializers import UserSerializer, UserUpdateSerializer

User = get_user_model()


class UsersListCreateView(generics.ListCreateAPIView):
    """Create and list users,
    can be used only by admins, agents and staff"""
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, AdminPermission | AgentPermission]


class UsersRUView(generics.RetrieveUpdateAPIView):
    """Edit and view details about user,
    can be used only by admins, agents and staff"""
    queryset = User.objects.all()
    serializer_class = UserUpdateSerializer
    permission_classes = [IsAuthenticated, AdminPermission | AgentPermission]
