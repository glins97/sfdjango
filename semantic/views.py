from rest_framework.decorators import api_view
from rest_framework.response import Response

from semantic.models import KipoOntology

@api_view(['POST'])
def querySPARQ(request):
    if request.method == 'POST':
        if request.data["query"]:
            ret = KipoOntology.querySPARQL(request.data["query"])
            return Response(ret, status=201)
        else:
            return Response(request.data, status=404)
