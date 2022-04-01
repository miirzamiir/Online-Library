from django.urls import path
from .views import CreateUserAPI, ManageUserAPI

urlpatterns = [
    path('create/', CreateUserAPI.as_view()),
    path('me/', ManageUserAPI.as_view()),
]