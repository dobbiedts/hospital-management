from rest_framework import serializers

from .models import Patient_Directory, Doctor_Directory, Assigned_Patient, Assigned_Doctor, Instance


class Doctor_DirectorySerializer(serializers.HyperlinkedModelSerializer):
   
    def to_representation(self, instance):
        if isinstance(instance, Assigned_Patient):
            return Assigned_PatientSerializer(instance=instance).data
        
    class Meta:
        model = Doctor_Directory
        fields = ('first_name', 'last_name', 'age', 'specialty')

class Patient_DirectorySerializer(serializers.HyperlinkedModelSerializer):
    def to_representation(self, instance):
        if isinstance(instance, Assigned_Doctor):
            return Assigned_DoctorSerializer(instance=instance).data
        
    class Meta:
        model = Patient_Directory
        fields = ('id', 'name', 'date', 'diagnosis', 'date', 'summary')
        
class Assigned_PatientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Assigned_Patient
        fields = '__all__'
        
        
class Assigned_DoctorSerializer(serializers.HyperlinkedModelSerializer):
     class Meta:
        model = Assigned_Doctor
        fields = '__all__'

class InstanceSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Instance
        fields = ('id', 'patient', 'doctor', 'date', 'operator')

        