from django_filters.rest_framework import FilterSet
from .models import Author, Book, Rent

class AuthorFilter(FilterSet):
    
    class Meta:
        model = Author
        fields = {
            'nationality' : ['exact'],
            'is_alive' : ['exact'],
            'rating' : ['gt' , 'lt']
        }


class BookFilter(FilterSet):

    class Meta:
        model = Book
        fields = {
            'categories' : ['exact'],
            'authors' : ['exact'],
            'translators' : ['exact'],
            'publisher' : ['exact'],
            'rating' :['gt', 'lt'],
            'unit_price' :['gt', 'lt'],
            'price_per_day' :['gt', 'lt'],
            'date_of_publish' : ['exact']
        }


class RentFilter(FilterSet):

    class Meta:
        model = Rent
        fields = {
            'is_returned' : ['exact'],
        }