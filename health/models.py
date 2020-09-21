from django.db import models
import uuid 
from django.contrib.auth.models import User
from datetime import date
from django.contrib.auth.models import User

class Doctor_Directory(models.Model):
    """Models representing  directory of doctors."""

    #fields
    #register the names of doctors in the directory
    first_name = models.CharField(max_length = 200, help_text = 'enter first name')
    last_name = models.CharField(max_length = 200, help_text = 'enter last name')
    age = models.IntegerField(help_text = 'Enter doctor age', default = None)
    specialty = models.CharField(max_length = 100, default = None)
    
    class Meta:
       
        ordering = ['last_name', 'first_name']

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.last_name}, {self.first_name}'
    class Admin:
        pass
    
class Patient_Directory(models.Model):
    id = models.UUIDField(primary_key = True, default= uuid.uuid4, help_text ='Unique id for this patient', editable = False )
    name = models.CharField(max_length = 100, help_text = "Enter patient's name")
    diagnosis = models.CharField(max_length = 100, help_text = "Enter patient's diagnosis")
    date = models.DateField(null = True, blank = True)
    summary = models.TextField(max_length=1000, help_text='Enter a brief description of the ailment')
    age = models.IntegerField(help_text = "Enter patients age", default = None)
    
   
    def __str__(self):
        
        return self.name
        return self.diagnosis
        return self.summary
        return self.date
    
    class Admin:
        pass
    
class Assigned_Doctor(Doctor_Directory):
   
    assigned_patient = models.ManyToManyField(Patient_Directory, help_text = 'who is/are the patients assigned to this doctor', default = None)
    
    
    
    class Meta:
        ordering = ['last_name', 'first_name']
    
    def get_absolute_url(self):
        """Returns the url to access a particular doctor instance."""
        return reverse('doctor-detail', args=[str(self.id)])
        
    def __str__(self):
        return f'{self.last_name}, {self.first_name}'
        return self.assigned_patient
        return self.specialty
    
    def display_assigned_patient(self):
        """Create a string for the assigned_patient. This is required to display assigned_patient in Admin."""
        return ', '.join(assigned_patient.name for assigned_patient in self.assigned_patient.all()[:3])
    
    display_assigned_patient.short_description = 'assigned_patient'  
    


class Assigned_Patient(Patient_Directory):
    assigned_doctor = models.ManyToManyField(Doctor_Directory, help_text = 'who is/are the patients assigned to this doctor', default = None)
    
    
    def __str__(self):
         
        return self.name
        return self.assigned_doctor
        return self.diagnosis
        return self.summary
        return self.date
    
    def get_absolute_url(self):
        """Returns the url to access a detail record for this patient."""
        return reverse('patient-detail', args=[str(self.id)])
    
    def display_assigned_doctor(self):
        """Create a string for the assigned_doctor. This is required to display assigned_doctor in Admin."""
        return ', '.join(assigned_doctor.first_name for assigned_doctor in self.assigned_doctor.all()[:3])
    
    display_assigned_doctor.short_description = 'assigned_doctor'        

    

class Instance(models.Model):
    """Model representing specific details of particular patient (i.e. that """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular case in the hospital')
    patient = models.ForeignKey('Assigned_Patient', on_delete=models.SET_NULL, null=True) 
    doctor = models.ForeignKey('Assigned_Doctor', on_delete=models.SET_NULL, null=True) 
    date = models.DateField(null=True, blank=True)
    operator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    
    
    
    patient_status =(
      ('r',  'receiving treatment'),
      ('d', 'discharged'),
      ('a', 'admitted'),
      ('ar', 'admitted and receiving treatment')
    )
    
    status = models.CharField(
       max_length = 3,
       choices = patient_status,
       blank = True,
       default = 'r',
       help_text = "patient status"
        
    )
        
        
    class Meta:
        ordering = ['date']
        permissions = (("can_mark_admitted", "Set patient as admitted"),("can_mark_as_discharged", "Set Patient as discharged"),)     

    
    def __str__(self):
        """String for representing the Model object"""
        return f'{self.id}({self.patient.assigned_doctor})'
    
    
    
        


    
    

    