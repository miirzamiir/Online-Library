from uuid import uuid4
from datetime import datetime
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django_countries.fields import CountryField
from django.conf import settings


class Author(models.Model):
    name = models.CharField(max_length=255)
    nationality = CountryField(null=True)
    rating = models.DecimalField(null=True,
                                 max_digits=3,
                                 decimal_places=2,
                                 validators=[
                                    MinValueValidator(0.00),
                                    MaxValueValidator(5.00)
                                    ]
                                )
    birth_date = models.PositiveSmallIntegerField(null=True)
    is_alive = models.BooleanField(default=True, null=True)
    description = models.TextField(null=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ('name', 'birth_date')


class Publisher(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255, null=True)
    telephone_number = models.CharField(max_length=30, null=True)
    description = models.TextField(null=True)

    def __str__(self) -> str:
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(null=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ('name',)


class Book(models.Model):
    title = models.CharField(max_length=240)
    publisher = models.ForeignKey(to=Publisher, on_delete=models.CASCADE)
    categories = models.ManyToManyField(to=Category)
    authors = models.ManyToManyField(to=Author, related_name='authors')
    translators = models.ManyToManyField(to=Author, related_name='translators', blank=True)
    inventory = models.PositiveSmallIntegerField(validators=[MinValueValidator(0)])
    description = models.TextField(null=True)
    rating = models.DecimalField(null=True,
                                 max_digits=3,
                                 decimal_places=2,
                                 validators=[
                                    MinValueValidator(0.00),
                                    MaxValueValidator(5.00)
                                    ]
                                )
    price_per_day =  models.DecimalField(max_digits=4,
                                 decimal_places=2,
                                 validators=[MinValueValidator(0.00)]
                                )
    unit_price = models.DecimalField(max_digits=5,
                                 decimal_places=2,
                                 validators=[MinValueValidator(0.00)]
                                )
    date_of_publish = models.PositiveSmallIntegerField()
    
    def __str__(self) -> str:
        return self.title


class BookImage(models.Model):
    book = models.ForeignKey(to=Book, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='library/books')


class Request(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
    book = models.ForeignKey(to=Book, on_delete=models.DO_NOTHING)
    date = models.DateTimeField(auto_now=True)
    rented = models.BooleanField(default=False)
    

class Rent(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    request = models.ForeignKey(to=Request, on_delete=models.CASCADE)
    borrow_date = models.DateTimeField(default=datetime.now)
    return_date = models.DateTimeField(null=True)
    is_returned = models.BooleanField(default=False)
    price_per_day =  models.DecimalField(max_digits=4,
                                 decimal_places=2,
                                 validators=[MinValueValidator(0.00)]
                                )
