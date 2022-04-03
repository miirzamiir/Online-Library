from django_countries.serializer_fields import CountryField
from django_countries.serializers import CountryFieldMixin
from rest_framework.serializers import ModelSerializer
from .models import Author, Publisher


class AuthorSerializer(ModelSerializer):

    nationality = CountryField(name_only=True)

    class Meta:
        model = Author
        fields = ('id', 'name', 'nationality', 'rating', 'birth_date', 'is_alive', 'description')


class PublisherSerializer(ModelSerializer):

    class Meta:
        model = Publisher
        fields = ('id', 'name', 'address', 'telephone_number', 'description')
