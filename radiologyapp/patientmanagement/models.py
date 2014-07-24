from django.db import models

# Create your models here.

class Patients(models.Model):

    first_name = models.CharField(
        max_length=255,
    )
    last_name = models.CharField(
        max_length=255,

    )
    ref_doc = models.CharField(
        max_length=255,

    )
    phone = models.IntegerField()	
    email = models.EmailField()

    def __str__(self):

        return ' '.join([
            self.first_name,
            self.last_name,
        ])
