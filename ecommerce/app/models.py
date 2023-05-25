from django.db import models

# Create your models here.
class Category(models.Models):
    name = models.CharField(max_length=50)
    
    @staticmethod
    def get_all_categories():
        return Category.objects.all()
    
    def __str__(self):
        return self.name
    