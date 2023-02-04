from rest_framework import serializers
from backend.models import Author, Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title']


class AuthorSerializer(serializers.ModelSerializer):
    book = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='title'
    )

    class Meta:
        model = Author
        fields = ['id', 'name', 'book']

