from .permissions import AdminPermission, AgentPermission
from rest_framework import generics
from .serializers import UserSerializer, UserUpdateSerializer
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated

User = get_user_model()


class UsersListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, AdminPermission | AgentPermission]


class UsersRUView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserUpdateSerializer
    permission_classes = [IsAuthenticated, AdminPermission | AgentPermission]
