from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Patient(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="patients")
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    gender= models.CharField(max_length=10, choices=[
        ('Male','Male'),
        ('Female','Female'),
        ('Other','Other'),])
    phone= models.CharField(max_length=15,unique=True)
    address= models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.name}"

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    license_no = models.CharField(unique = True, max_length=35)
    phone= models.CharField(max_length=15)
    email= models.EmailField(unique=True)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Dr. {self.name}"

class PatientDoctorMappings(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="Doctor_mappings")
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name="Patient_mappings")
    assigned = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('patient', 'doctor')
    
    def __str__(self):
        return f"{self.patient} - {self.doctor}"
    