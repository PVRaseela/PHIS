from django.db import models

class DoctorSchedule(models.Model):
    doctorid=models.ForeignKey('administration.Employee', on_delete=models.CASCADE)
    doctor_name=models.CharField(max_length=122)
    availableday=models.CharField(max_length=122)
    startsat=models.DateTimeField()
    endsat=models.DateTimeField()
    noofslots=models.IntegerField()

class Encounter(models.Model):
    patientid=models.ForeignKey('registration.Patient', on_delete=models.CASCADE)
    # _(followup/revisit/firstvisit)
    visit_status=models.CharField(max_length=122)
    # confirms/booked 
    encounter_status=models.CharField(max_length=122)
    consulting_doctor=models.CharField(max_length=122)    

class PatientVisit(models.Model):
    patientid=models.ForeignKey('registration.Patient', on_delete=models.CASCADE)
    visitno=models.CharField(max_length=122)
    # ip op
    visit_type=models.CharField(max_length=122)
    # revisit/firstvisit
    visit_status=models.CharField(max_length=122)

    consulting_doctor=models.CharField(max_length=122)
    encounterid=models.ForeignKey(Encounter, on_delete=models.CASCADE)

