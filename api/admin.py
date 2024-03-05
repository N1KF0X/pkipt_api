from django.contrib import admin

from . import models


class EnrolleeAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'snils', 'inn', 'gpa', 'current_id', 'application_date']
    search_fields = ['full_name', 'snils', 'inn', 'gpa', 'application_date']
    list_editable = ['gpa', 'application_date']


class SpecialityAdmin(admin.ModelAdmin):
    list_display = ['name', 'seats_amount']
    search_fields = ['name']


class EnrolleeSpecialityAdmin(admin.ModelAdmin):
    list_display = [
        'enrollee_snils',
        'speciality_name',
        'priority',
        'is_enrolled',
    ]
    search_fields = [
        'enrollee_snils',
        'speciality_name',
    ]
    list_filter = ['priority', 'speciality_name', 'is_enrolled']


class CurrentAdmin(admin.ModelAdmin):
    list_display = ['number', 'year', 'is_open']
    search_fields = ['year']
    list_filter = ['year']


admin.site.register(models.Enrollee, EnrolleeAdmin)
admin.site.register(models.Speciality, SpecialityAdmin)
admin.site.register(models.EnrolleeSpeciality, EnrolleeSpecialityAdmin)
admin.site.register(models.Current, CurrentAdmin)

admin.site.site_header = 'Учёт абитуриентов'
admin.site.site_title = 'Учёт абитуриентов'