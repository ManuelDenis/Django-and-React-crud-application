from rest_framework import generics
from backend.models import Author
from backend.serializers import AuthorSerializer


class AuthorList(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
