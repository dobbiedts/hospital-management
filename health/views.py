from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from .serializers import Patient_DirectorySerializer, Doctor_DirectorySerializer, Assigned_PatientSerializer, Assigned_DoctorSerializer,   InstanceSerializer

from .models import Patient_Directory, Doctor_Directory, Assigned_Patient, Assigned_Doctor, Instance


class Doctor_DirectoryViewSet(viewsets.ModelViewSet):
    queryset = Doctor_Directory.objects.all().order_by('first_name')
    serializer_class = Doctor_DirectorySerializer
    
class Patient_DirectoryViewSet(viewsets.ModelViewSet):
    queryset = Patient_Directory.objects.all().order_by('name')
    serializer_class = Patient_DirectorySerializer
    
class Assigned_DoctorViewSet(viewsets.ModelViewSet):
    queryset = Assigned_Doctor.objects.all().order_by('first_name')
    serializer_class = Assigned_DoctorSerializer

class Assigned_PatientViewSet(viewsets.ModelViewSet):
    queryset = Assigned_Patient.objects.all().order_by('name')
    serializer_class = Assigned_PatientSerializer
    
class InstanceViewSet(viewsets.ModelViewSet):
    queryset = Instance.objects.all().order_by('id')
    serializer_class = InstanceSerializer
    