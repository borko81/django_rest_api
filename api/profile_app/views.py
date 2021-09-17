from rest_framework import views, status, filters
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication

from .models import UserProfile
from .serializers import ApiSerializer, ViewsetSerializer, UserProfileSerialzier
from .permissions import UpdateOwnPrfile


class HelloViewSet(viewsets.ViewSet):
    serizlier_class = ViewsetSerializer

    def list(self, request):
        l_message = "This is a message"
        return Response({"message": l_message})

    def create(self, request):
        serialzier = self.serizlier_class(data=request.data)
        if serialzier.is_valid():
            name = serialzier.validated_data.get("name")
            message = "It looked correct"
            return Response({"message": message, "name": name}, status=status.HTTP_201_CREATED)
        return Response(serialzier.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        return Response({"method": "retrieve"})

    def update(self, request, pk=None):
        return Response({"method": "update"})

    def partial_update(self, request, pk=None):
        return Response({"method": "partial_update"})

    def destroy(self, request, pk=None):
        return Response({"method": "destory"})


class HelloView(views.APIView):

    serializer_class = ApiSerializer

    def get(self, request, format=None):
        l_message = "This is a message"
        return Response({"message": l_message})

    def post(self, request):
        serializier = self.serializer_class(data=request.data)

        if serializier.is_valid():
            name = serializier.validated_data.get("name")
            message = f"Hello {name}"
            return Response({"message": message}, status=status.HTTP_201_CREATED)
        return Response(serializier.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, requst, pk=None):
        return Response({"method": "put"})

    def patch(self, request, pk=None):
        return Response({"methor": "patch"})

    def delete(self, request, pk=None):
        return Response({"method": "delete"})


class UserProfileViewSet(viewsets.ModelViewSet):
    serializer_class = UserProfileSerialzier
    queryset = UserProfile.objects.all()
    authentication_classes = (TokenAuthentication, )
    permission_classes = (UpdateOwnPrfile, )
    filter_backends = (filters.SearchFilter, )
    search_fields = ('name', 'name')
