from rest_framework import generics
from backend.models import Author
from backend.serializers import AuthorSerializer
from django.shortcuts import render


def index(request):
    return render(request, "build/index.html")


class AuthorList(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
