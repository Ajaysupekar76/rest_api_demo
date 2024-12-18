from django.db import models

# Create your models here.
class Company(models.Model):
    IT = 'IT'
    NON_IT = 'Non-IT'

    COMPANY_TYPE_CHOICES = [
        (IT, 'IT'),
        (NON_IT, 'Non-IT'),
    ]

    company_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    about = models.TextField()
    type = models.CharField(max_length=10, choices=COMPANY_TYPE_CHOICES)
    added_date = models.DateField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name