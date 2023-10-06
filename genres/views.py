from drf_spectacular.utils import extend_schema
from rest_framework import status, viewsets
from rest_framework.response import Response

from .models import Genre
from .serializers import GenreSerializer


# Create your views here.
class GenreViewSet(viewsets.ViewSet):
    """
    A simple viewset for viewing genres
    """

    queryset = Genre.objects.all()

    @extend_schema(responses=GenreSerializer, tags=["Genres"], summary="Returns list of Genres")
    def list(self, request):
        genres = Genre.objects.all()
        serializer = GenreSerializer(genres, many=True)
        return Response(serializer.data)

    @extend_schema(request=GenreSerializer, responses=GenreSerializer, tags=["Genres"], summary="Creates Genre")
    def create(self, request):
        serializer = GenreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @extend_schema(responses=GenreSerializer, tags=["Genres"], summary="Removes Genre")
    def destroy(self, request, pk=None):
        try:
            genre = Genre.objects.get(pk=pk)
        except Genre.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        genre.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @extend_schema(responses=GenreSerializer, tags=["Genres"], summary="Returns Genre")
    def retrieve(self, request, pk=None):
        try:
            genre = Genre.objects.get(pk=pk)
        except Genre.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = GenreSerializer(genre)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @extend_schema(request=GenreSerializer, responses=GenreSerializer, tags=["Genres"], summary="Updates Genre")
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
