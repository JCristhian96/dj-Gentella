from django.urls import path
# Views
from . import views

app_name = "users"

urlpatterns = [
    path(
        'register/',
        views.UserCreateView.as_view(),
        name="register"
    ),
    path(
        'login/',
        views.LoginView.as_view(),
        name="login"
    ),
    path(
        'logout/',
        views.LogoutView.as_view(),
        name="logout"
    )
]