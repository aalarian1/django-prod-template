from django.db import models

# Create your models here.
class Business(models.Model):
    class Price_Range(models.TextChoices):
        Cheap = ("cheap", "Cheap")
        Affordable = ("affordable", "Affordable")
        Expensive = ("expensive", "Expensive")
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    category = models.CharField(max_length=20)
    location = models.CharField(max_length=50)
    price_range = models.CharField(max_length=12, choices=Price_Range.choices)
    rating = models.FloatField()
    def average_rating(self):
        # get all the reviews for this restaurant
        reviews = Business.objects.filter(business=self)
        # calculate the average rating
        ratings = [review.rating for review in reviews]
        if len(ratings) > 0:
            return sum(ratings) / len(ratings)
        else:
            return None
    def __str__(self):
        return self.name
