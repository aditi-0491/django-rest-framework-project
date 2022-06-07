from django.db import models

class FoodLog(models.Model):
    item = models.TextField(null=True, blank=False)
    carbs = models.FloatField(null=True, blank=False)
    fats = models.FloatField(null=True, blank=False)
    protein = models.FloatField(null=True, blank=False)
    calories = models.IntegerField(null=True, blank=False)
 
    def __str__(self):
        return self.title

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['item'], name='item')
        ]