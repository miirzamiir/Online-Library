from django_countries.serializer_fields import CountryField
from django_countries.serializers import CountryFieldMixin
from django_countries.data import COUNTRIES
from rest_framework import serializers
from .models import Author


class AuthorSerializer(serializers.ModelSerializer, CountryFieldMixin):

    nationality = CountryField(name_only=True)

    class Meta:
        model = Author
        fields = ('id', 'name', 'nationality', 'rating', 'birth_date', 'is_alive', 'description')

    