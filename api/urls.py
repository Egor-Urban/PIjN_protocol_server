from django.urls import path
from .views import hello, ping

urlpatterns = [
    path("hello/", hello, name="hello"),
    path("ping/", ping, name="ping"),
]

