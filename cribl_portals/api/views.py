from rest_framework.response import Response
from rest_framework.decorators import api_view
from elastic.models import ElasticDestination
from .serializers import ElasticSerializer

@api_view(["GET"])
def getData(request):
    clusters = ElasticDestination.objects.all()
    serializer = ElasticSerializer(clusters, many=True)
    return Response(serializer.data)

@api_view(["POST"])
def add_cluster(request):
    serializer = ElasticSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)