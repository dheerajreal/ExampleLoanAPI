
from django.urls import path
from .views import UsersListCreateView, UsersRUView

urlpatterns = [
    path('', UsersListCreateView.as_view(), name="user_list_create"),
    path('<pk>/', UsersRUView.as_view(), name="user_read_update"),

]
