# Generated by Django 4.0.4 on 2022-07-05 16:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('registration', '0007_remove_doctorschedule_doctorid_and_more'),
        ('administration', '0001_initial'),
        ('appointment', '0002_delete_hospital'),
    ]

    operations = [
        migrations.CreateModel(
            name='Encounter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visit_status', models.CharField(max_length=122)),
                ('encounter_status', models.CharField(max_length=122)),
                ('consulting_doctor', models.CharField(max_length=122)),
                ('patientid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registration.patient')),
            ],
        ),
        migrations.CreateModel(
            name='PatientVisit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visitno', models.CharField(max_length=122)),
                ('visit_type', models.CharField(max_length=122)),
                ('visit_status', models.CharField(max_length=122)),
                ('consulting_doctor', models.CharField(max_length=122)),
                ('encounterid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appointment.encounter')),
                ('patientid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registration.patient')),
            ],
        ),
        migrations.CreateModel(
            name='DoctorSchedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctor_name', models.CharField(max_length=122)),
                ('availableday', models.CharField(max_length=122)),
                ('startsat', models.DateTimeField()),
                ('endsat', models.DateTimeField()),
                ('noofslots', models.IntegerField()),
                ('doctorid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administration.employee')),
            ],
        ),
    ]
