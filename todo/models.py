from django.db import models
from django.utils import timezone
from django.db.models import CheckConstraint, Q

# Create your models here.
class Todo(models.Model):
  title= models.CharField(max_length=1000, null=False, blank=False)
  priority = models.IntegerField(null=True, blank=True)  
  due_date = models.DateField( default=timezone.now)



  def __str__(self) :
    return self.title