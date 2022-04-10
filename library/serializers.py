from datetime import datetime
from django_countries.serializer_fields import CountryField
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from django.db.models import F
from .models import Author, Book, BookImage, Category, Publisher, Rent, Request


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


class BookImageSerializer(ModelSerializer):

    def create(self, validated_data):
        validated_data['book_id'] = self.context.get('book_id')
        return super().create(validated_data)

    class Meta:
        model = BookImage
        fields = ('id', 'image')


class BookSerializer(ModelSerializer):

    images = BookImageSerializer(many=True, read_only=True)

    class Meta:
        model = Book
        fields = (
                'id', 'title', 'categories', 'publisher', 'authors',
                'translators', 'inventory', 'rating','unit_price',
                'price_per_day', 'date_of_publish', 'description', 'images'
            )


class RetrieveBookSerializer(BookSerializer):
    
    authors = AuthorSerializer(many=True, read_only=True)
    translators = AuthorSerializer(many=True, read_only=True)
    categories = CategorySerializer(many=True, read_only=True)
    publisher = PublisherSerializer(read_only=True)


class RequestSerializer(ModelSerializer):

    def create(self, validated_data):

        validated_data['user'] = self.context.get('request').user
        return super().create(validated_data)


    class Meta:
        model = Request
        fields = ['id', 'book', 'date']
        read_only_fields = ('user', 'date')


class GetRequestSerializer(RequestSerializer):

    book = serializers.HyperlinkedRelatedField(view_name='book-detail', read_only=True)

    class Meta(RequestSerializer.Meta):
      RequestSerializer.Meta.fields.append('user')


class AdminRequestSerializer(ModelSerializer):

    def get_inventory(self, obj):
        return obj.book.inventory

    book = serializers.HyperlinkedRelatedField(view_name='book-detail', read_only=True)
    inventory = serializers.SerializerMethodField(method_name='get_inventory')

    def update(self, instance, validated_data):
        if instance.book.inventory==0:
            raise ValueError("can't rent this book because it's inventory is less than 1.")
        
        return super().update(instance, validated_data)


    class Meta:
        model = Request
        fields = ('id', 'user', 'book', 'date', 'rented', 'inventory')
        read_only_fields = ('user', 'date', 'book')
        extra_kwargs = {
            'rented' : {'write_only' : True}
        }


class RentSerializer(ModelSerializer):
    
    def get_total_price(self, instance):
        
        borrow_date = instance.borrow_date.date()
        price = instance.price_per_day

        if instance.is_returned:
            return_date = instance.return_date.date()

            return price*((return_date-borrow_date).days+1)

        now = datetime.now().date()
        return  price*((now-borrow_date).days+1)


    request = GetRequestSerializer()
    total_price = serializers.SerializerMethodField()
   
   
    class Meta:
        model = Rent
        fields = ('id', 'borrow_date', 'return_date',
                  'is_returned', 'price_per_day', 'request', 'total_price'
        )


class UpdateRentSerializer(ModelSerializer):    
    
    def update(self, instance, validated_data):
        validated_data['return_date'] = datetime.now()
        return super().update(instance, validated_data)

    def validate_is_returned(self, value):
        if value == False:
            raise ValueError("can't turn is_returned back to False!")

        return value

        
    class Meta:
        model = Rent
        fields = ('is_returned',)