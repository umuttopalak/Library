from django.db import models

from authors.models import Author
from genres.models import Genre


# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=50)
    page_number = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']
