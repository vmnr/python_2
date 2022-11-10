from distutils.command.upload import upload
from django.db import models

# Create your models here.
class Employee(models.Model):
    employee_id = models.PositiveIntegerField(primary_key = True)
    first_name = models.CharField(max_length = 30 ,blank=True, null=True)
    last_name =models.CharField(max_length = 30,blank=True, null=True ) 
    email_id = models.EmailField(blank=True, null=True)
    phone_number = models.CharField(max_length = 10, blank=True, null=True)        
    date_of_birth = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.employee_id}-{self.first_name}-{self.last_name}-{self.email_id}-{self.phone_number}-{self.date_of_birth}"

