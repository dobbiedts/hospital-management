from rest_framework import serializers

from .models import Patient_Directory, Doctor_Directory, Assigned_Patient, Assigned_Doctor, Instance


class Doctor_DirectorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Doctor_Directory
        fields = ('first_name', 'last_name', 'age', 'specialty')
        
        
class Patient_DirectorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Patient_Directory
        fields = ('id', 'name', 'date', 'diagnosis', 'date', 'summary')
        
class Assigned_PatientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Assigned_Patient
        fields = ('assigned_doctor')
        
        
class Assigned_DoctorSerializer(serializers.HyperlinkedModelSerializer):
     class Meta:
        model = Assigned_Doctor
        fields = ('assigned_patient')

class InstanceSerializer(serializers.HyperlinkedModelSerializer):
     class Meta:
        model = Instance
        fields = ('id', 'patient', 'doctor', 'date', 'operator')

        