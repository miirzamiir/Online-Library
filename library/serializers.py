from django_countries.serializer_fields import CountryField
from rest_framework.serializers import ModelSerializer
from .models import Author, Book, Category, Publisher, Rent


class AuthorSerializer(ModelSerializer):

    nationality = CountryField(name_only=True)

    class Meta:
        model = Author
        fields = ('id', 'name', 'nationality', 'rating', 'birth_date', 'is_alive', 'description')


class PublisherSerializer(ModelSerializer):

    class Meta:
        model = Publisher
        fields = ('id', 'name', 'address', 'telephone_number', 'description')


class CategorySerializer(ModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'name', 'description')


class BookSerializer(ModelSerializer):

    def create(self, validated_data):

        validated_data['slug'] = str(validated_data['title']).strip().replace(' ','_')
        return super().create(validated_data)

    def update(self, instance, validated_data):
        
        title = validated_data.get('title')
        if title:
            validated_data['slug'] = str(validated_data['title']).strip().replace(' ','_')

        return super().update(instance, validated_data)

    class Meta:
        model = Book
        fields = (
                'id', 'title', 'categories', 'publisher', 'authors',
                'translators', 'inventory', 'rating', 'unit_price',
                'price_per_day', 'date_of_publish', 'description'
            )


class RetrieveBookSerializer(BookSerializer):
    
    authors = AuthorSerializer(many=True, read_only=True)
    translators = AuthorSerializer(many=True, read_only=True)
    categories = CategorySerializer(many=True, read_only=True)
    publisher = PublisherSerializer(read_only=True)

