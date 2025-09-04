
from django.urls import path, include
from api.views import ping

urlpatterns = [
    path("ping/", ping)
]
