from rest_framework.response import Response
from rest_framework.decorators import api_view
from elastic.models import ElasticDestination, ElasticDestinationUpdate
from .serializers import ElasticSerializer

@api_view(["GET"])
def elastic_get(request):
    destinations = ElasticDestination.objects.all()
    serializer = ElasticSerializer(destinations, many=True)
    return Response(serializer.data)

@api_view(["POST"])
def elastic_update(request, pk):

    destination = ElasticDestination.objects.get(id=pk)

    if "title" in request.data and not destination.title == request.data["title"]:
        destination.title = request.data["title"]
    if "description" in request.data and not destination.description == request.data["description"]:
        destination.description = request.data["description"]
    if "username" in request.data and not destination.username == request.data["username"]:
        destination.username = request.data["username"]
    if "password" in request.data and not destination.password == request.data["password"]:
        destination.password = request.data["password"]
    if "url" in request.data and not destination.url == request.data["url"]:
        destination.url = request.data["url"]
    if "message" in request.data and not destination.message == request.data["message"]:
        destination.message = request.data["message"]
    if "status" in request.data and not destination.status == request.data["status"]:
        destination.status = request.data["status"]
    
    destination.save()
    serializer = ElasticSerializer(destination)
    return Response(serializer.data)