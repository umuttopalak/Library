from django.shortcuts import render
from drf_spectacular.utils import extend_schema
from rest_framework import status, viewsets
from rest_framework.response import Response

from .models import Author, Book, Genre
from .serializers import AuthorSerializer, BookSerializer, GenreSerializer


# Create your views here.
class GenreViewSet(viewsets.ViewSet):
    """
    A simple viewset for viewing genres
    """

    queryset = Genre.objects.all()

    @extend_schema(responses=GenreSerializer, tags=["Genres"])
    def list(self, request):
        genres = Genre.objects.all()
        serializer = GenreSerializer(genres, many=True)
        return Response(serializer.data)

    @extend_schema(request=GenreSerializer, responses=GenreSerializer, tags=["Genres"])
    def create(self, request):
        serializer = GenreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @extend_schema(responses=GenreSerializer, tags=["Genres"])
    def destroy(self, request, pk=None):
        try:
            genre = Genre.objects.get(pk=pk)
        except Genre.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        genre.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @extend_schema(responses=GenreSerializer, tags=["Genres"])
    def retrieve(self, request, pk=None):
        try:
            genre = Genre.objects.get(pk=pk)
        except Genre.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = GenreSerializer(genre)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @extend_schema(request=GenreSerializer, responses=GenreSerializer, tags=["Genres"])
    def update(self, request, pk=None):
        try:
            genre = Genre.objects.get(pk=pk)
        except Genre.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = GenreSerializer(genre, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AuthorViewSet(viewsets.ViewSet):
    """
    A simple viewset for viewing authors
    """
    queryset = Author.objects.all()

    @extend_schema(responses=AuthorSerializer, tags=["Authors"])
    def list(self, request):
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        return Response(serializer.data)

    @extend_schema(request=AuthorSerializer, responses=AuthorSerializer, tags=["Authors"])
    def create(self, request):
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @extend_schema(responses=AuthorSerializer, tags=["Authors"])
    def destroy(self, request, pk=None):
        try:
            author = Author.objects.get(pk=pk)
        except Author.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        author.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @extend_schema(responses=AuthorSerializer, tags=["Authors"])
    def retrieve(self, request, pk=None):
        try:
            author = Author.objects.get(pk=pk)
        except Author.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = AuthorSerializer(author)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @extend_schema(request=AuthorSerializer, responses=AuthorSerializer, tags=["Authors"])
    def update(self, request, pk=None):
        try:
            author = Author.objects.get(pk=pk)
        except Author.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = AuthorSerializer(author, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookViewSet(viewsets.ViewSet):
    """
    A simple viewset for viewing books
    """
    queryset = Book.objects.all()

    @extend_schema(responses=BookSerializer, tags=['Books'])
    def list(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    @extend_schema(request=BookSerializer, responses=BookSerializer, tags=["Books"])
    def create(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @extend_schema(responses=BookSerializer, tags=["Books"])
    def destroy(self, request, pk=None):
        try:
            book = Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @extend_schema(request=BookSerializer, responses=BookSerializer, tags=["Books"])
    def retrieve(self, request, pk=None):
        try:
            book = Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = BookSerializer(book)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @extend_schema(request=BookSerializer, responses=BookSerializer, tags=["Books"])
    def update(self, request, pk=None):
        try:
            book = Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = BookSerializer(book, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
