from django_filters.rest_framework import FilterSet
from .models import Author

class AuthorFilter(FilterSet):
    
    class Meta:
        model = Author
        fields = {
            'nationality' : ['exact'],
            'is_alive' : ['exact'],
            'rating' : ['gt' , 'lt']
        }