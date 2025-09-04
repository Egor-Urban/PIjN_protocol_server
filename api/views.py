from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(["GET"])
def hello(request):
    return Response({"status": "ok"})

@api_view(["GET"])
def ping(request):
    return Response({"status": "ok"})
