from django.db import models

# Create your models here.
class Hospital(models.Model):
    hospital_name= models.CharField(max_length=122)
    hospital_address= models.TextField(max_length=200)

class Employee(models.Model):
    emp_name= models.CharField(max_length=122)
    firstname= models.CharField(max_length=122)
    middlename= models.CharField(max_length=122)
    lastname= models.CharField(max_length=122)
    emp_phone= models.CharField(max_length=12)
    emp_email= models.CharField(max_length=122)
    emp_designation= models.CharField(max_length=122)
    emp_address= models.TextField(max_length=200)
    organisationid= models.ForeignKey(Hospital, on_delete=models.CASCADE)

class UserRole(models.Model):
    Role_Name= models.CharField(max_length=122)
    

class User(models.Model):
    username= models.CharField(max_length=122)
    password= models.TextField(max_length=122)
    user_type= models.TextField(max_length=122)
    employee=models.ForeignKey(Employee, on_delete=models.CASCADE)
    role_id=models.ForeignKey(UserRole, on_delete=models.CASCADE)


class Services(models.Model):
    service_name=models.CharField(max_length=150)
    # doctor_fee,procedure,other service fee
    service_type=models.CharField(max_length=122)
    tariff=models.FloatField()
    