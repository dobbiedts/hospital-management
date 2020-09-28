from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'Doctor_Directory', views.Doctor_DirectoryViewSet)
router.register(r'Patient_Directory', views.Patient_DirectoryViewSet)
router.register(r'Assigned_Doctor', views.Assigned_DoctorViewSet)
router.register(r'Assigned_Patient', views.Assigned_PatientViewSet)
router.register(r'Instance', views.InstanceViewSet, basename = 'Instance')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]