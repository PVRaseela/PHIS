from django.db import models

# Create your models here.
class Consultation(models.Model):
    patientid=models.ForeignKey('registration.Patient', on_delete=models.CASCADE)
    patientdiagnosis=models.TextField(max_length=200)
    finaldiagnosis=models.TextField(max_length=200)
