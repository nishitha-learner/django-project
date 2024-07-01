from django.db import models

# Create your models here.

class Registration(models.Model):
    name = models.CharField(max_length=100)
    college = models.CharField(max_length=100)
    course = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} from {self.college} registered for {self.course}"