from django.http.response import Http404
from rest_framework.views import APIView
from rest_framework import views, status
from rest_framework.response import Response

from .serializers import ApiSerializer


class HelloView(views.APIView):

    serializer_class = ApiSerializer

    def get(self, request, format=None):
        l_message = "This is a message"
        return Response({'message': l_message})

    def post(self, request):
        serializier = self.serializer_class(data=request.data)

        if serializier.is_valid():
            name = serializier.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message}, status=status.HTTP_201_CREATED)
        return Response(serializier.errors, status=status.HTTP_400_BAD_REQUEST)
