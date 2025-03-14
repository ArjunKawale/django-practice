from django.db import models
from django.urls import reverse
from django.db.models import UniqueConstraint
from django.db.models.functions import Lower

class Genre(models.Model):
    name=models.CharField(max_length=200,unique=True,help_text="Enter a book Genre name")
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('genre-detail',args=[str(self.id)])
    
    class Meta:
       constraints=[UniqueConstraint(Lower('name'),name='genre_name_case_insensitive_unique',violation_error_message='Name already exists')]



class Book(models.Model):
    name=models.CharField(max_length=200)
    author=models.ForeignKey("Author", on_delete=models.RESTRICT,null=True)
    summary=models.TextField(_max_length=1000, help_text="Enter a brief description of the book")
    isbn = models.CharField('ISBN', max_length=13,
                            unique=True,
                            help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn'
                                      '">ISBN number</a>')
    genre = models.ManyToManyField(
        Genre, help_text="Select a genre for this book")
    def __str__(self):
        """String for representing the Model object."""
        return self.title

    def get_absolute_url(self):
        """Returns the URL to access a detail record for this book."""
        return reverse('book-detail', args=[str(self.id)])