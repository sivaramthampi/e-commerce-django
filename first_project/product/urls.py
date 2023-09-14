from django.urls import path
from . import views
urlpatterns = [
    path("", views.call),
    path("user",views.userInfo)
]