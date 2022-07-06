from django.db import models


# Create your models here.

class Patient(models.Model):
    patient_name=models.CharField(max_length=122)
    prno=models.CharField(max_length=122)
    mobile=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    dob=models.DateField()
    age=models.IntegerField()
    address=models.TextField(max_length=200)

class Patienthistory(models.Model):
    patientid=models.ForeignKey(Patient, on_delete=models.CASCADE)
    prevous_history=models.TextField(max_length=200)
    previous_doctor_remarks=models.TextField(max_length=200)
    cross_consultation=models.CharField(max_length=3)
    previous_doctor_details=models.TextField(max_length=200)


