#  makemigrations - sqlscript
#  migrate - execute
#  course -->    name,descriptions,durations
#  student  -->  name ,address,course(fk)

from django.db import models

class airport(models.Model):
    city=models.CharField(max_length=40)
    code=models.CharField(max_length=40)

    def __str__(self):
        return f"Airport - {self.city}({self.code})"


# Create your models here.
class flight(models.Model):
    origin = models.ForeignKey(airport,on_delete=models.CASCADE,related_name="departure")
    destion=models.ForeignKey(airport,on_delete=models.CASCADE,related_name="arrivals")
    duration=models.IntegerField()

    def __str__(self):
        return f"Flight ( {self.origin} to {self.destion})";
