from rest_framework.decorators import api_view
from rest_framework.response import Response
from utils.logger import log

@api_view(["GET"])
def ping(request):
    log.info("Получен запрос /ping/")
    return Response({"status": "ok"})
