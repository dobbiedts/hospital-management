from django.contrib import admin

# Register your models here.
from .models import Patient_Directory, Doctor_Directory, Assigned_Patient, Assigned_Doctor, Instance



class Assigned_DoctorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'specialty', 'age', 'display_assigned_patient')
    pass

# Register the admin class with the associated model
admin.site.register(Assigned_Doctor, Assigned_DoctorAdmin)


class InstanceInline(admin.TabularInline):
    model = Instance
    
@admin.register(Assigned_Patient)
class Assigned_PatientAdmin(admin.ModelAdmin):
    list_display = ('name', 'diagnosis', 'summary', 'age', 'date', 'display_assigned_doctor')
    inlines = [InstanceInline]
    pass
#admin.site.register(Assigned_PatientAdmin)


# Register the Admin classes for BookInstance using the decorator


    
@admin.register(Instance) 
class InstanceAdmin(admin.ModelAdmin):
    list_display = ('patient', 'status', 'doctor', 'id')
    list_filter = ('status', 'date')
    
    fieldsets = (
        (None, {
            'fields': ('patient', 'doctor', 'id')
        }),
        ('Status', {
            'fields': ('status', 'date', 'operator')
        }),
    )


admin.site.register(Doctor_Directory)
admin.site.register(Patient_Directory)




    
