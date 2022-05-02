from turtle import title
from django.db import models

# Create your models here.
class TODO(models.Model):
    created_on=models.DateTimeField(auto_now_add=True)
    title=models.CharField(max_length=50)
    description=models.TextField()
    is_Done=models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return self.title
