from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Review  

@receiver(post_save, sender=Review)
def update_restaurant_rating(sender, instance, **kwargs):
    instance.restaurant.update_average_rating()
