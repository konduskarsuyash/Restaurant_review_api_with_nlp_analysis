from django.db import models
from authentication.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from .nlp_utils import analyze_sentiment
from .leaderboard import Leaderboard


class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    location = models.CharField(max_length=100)
    city = models.CharField(max_length=20)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    average_rating = models.DecimalField(max_digits=3, decimal_places=2, default=0.00)  # New field for average rating
    
    def __str__(self):
        return self.name

    def update_average_rating(self):
        average = self.reviews.aggregate(models.Avg('rating'))['rating__avg']
        self.average_rating = round(average, 2) if average else 0
        self.save()

        leaderboard = Leaderboard('restaurant_leaderboard')
        leaderboard.add_score(self.id, float(self.average_rating))

        
        
class Review(models.Model):
    restaurant = models.ForeignKey(Restaurant, related_name='reviews', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.DecimalField(max_digits=3, decimal_places=1, validators=[MinValueValidator(1), MaxValueValidator(5)])
    comment = models.TextField()
    sentiment = models.CharField(max_length=10, blank=True)  
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs):
        # Analyze the sentiment of the comment
        self.sentiment = analyze_sentiment(self.comment)
        super(Review, self).save(*args, **kwargs)
        self.restaurant.update_average_rating()
    
    def __str__(self):
        return f"{self.user.username} - {self.restaurant.name} - {self.rating}"
