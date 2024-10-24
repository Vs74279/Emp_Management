from django.db import models

# Create your models here.
class Emp(models.Model):
    name=models.CharField(max_length=200)
    emp_id=models.CharField(max_length=100, default="EMP123")
    phone=models.CharField(max_length=12, default="0000000000")
    address=models.TextField(default="Unknown address")
    working=models.BooleanField(default=True)
    department=models.CharField(max_length=40, default="General")

    def __str__(self):
        return self.name