from django.db import models

# Create your models here.



class Employee(models.Model):
    name = models.CharField(max_length=200)
    salary = models.FloatField()

    class Meta:
        db_table = "employee"

    def __str__(self):
        return f'{self.id}-----{self.name}-----{self.salary}'


