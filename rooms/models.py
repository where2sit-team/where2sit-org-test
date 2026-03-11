from django.db import models

# Create your models here.

class Building(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Room(models.Model):
    building = models.ForeignKey(Building, on_delete=models.CASCADE)
    number = models.CharField(max_length=10)
    capacity = models.IntegerField()

    def __str__(self):
        return f"{self.building} - {self.number}"
