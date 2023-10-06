from drf_spectacular.utils import extend_schema
from rest_framework import status, viewsets
from rest_framework.response import Response

from .models import Author
from .serializers import AuthorSerializer


# Create your views here.
class AuthorViewSet(viewsets.ViewSet):
    """
    A simple viewset for viewing authors
    """
    queryset = Author.objects.all()

    @extend_schema(responses=AuthorSerializer, tags=["Authors"], summary="Returns list of Authors")
    def list(self, request):
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        return Response(serializer.data)

    @extend_schema(request=AuthorSerializer, responses=AuthorSerializer, tags=["Authors"], summary="Creates Author")
    def create(self, request):
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @extend_schema(responses=AuthorSerializer, tags=["Authors"], summary="Removes Author")
    def destroy(self, request, pk=None):
        try:
            author = Author.objects.get(pk=pk)
        except Author.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        author.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @extend_schema(responses=AuthorSerializer, tags=["Authors"], summary="Returns Author")
    def retrieve(self, request, pk=None):
        try:
            author = Author.objects.get(pk=pk)
        except Author.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = AuthorSerializer(author)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @extend_schema(request=AuthorSerializer, responses=AuthorSerializer, tags=["Authors"], summary="Updates Author")
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
