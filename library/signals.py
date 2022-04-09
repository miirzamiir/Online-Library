from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Book, Request, Rent

@receiver(post_save, sender=Request)
def create_rent(sender, **kwargs):
    if not kwargs.get('created', True):
        req:Request = kwargs.get('instance')
        Rent.objects.create(
            request = req,
            price_per_day = req.book.price_per_day
        )

@receiver(post_save, sender=Request)
def update_inventory_after_rent(sender, **kwargs):
    if not kwargs.get('created', True):
        book = kwargs.get('instance').book
        Book.objects.filter(id=book.id).update(inventory = book.inventory-1)