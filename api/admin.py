from django.contrib import admin

from . import models


class EnrolleeAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'snils', 'inn', 'gpa', 'recruitment', 'application_date']
    search_fields = ['full_name', 'snils', 'inn', 'gpa', 'application_date']


class SpecialityAdmin(admin.ModelAdmin):
    list_display = ['name', 'seats_amount']
    search_fields = ['name']


class EnrolleeSpecialityAdmin(admin.ModelAdmin):
    list_display = [
        'enrollee',
        'speciality',
        'is_priority',
        'is_enrolled',
    ]
    search_fields = ['enrollee']
    list_filter = ['speciality', 'is_priority', 'is_enrolled']


class RecruitmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'closing_date']
    search_fields = ['name']


admin.site.register(models.Enrollee, EnrolleeAdmin)
admin.site.register(models.Speciality, SpecialityAdmin)
admin.site.register(models.EnrolleeSpeciality, EnrolleeSpecialityAdmin)
admin.site.register(models.Recruitment, RecruitmentAdmin)

admin.site.site_header = 'ПКИПТ API'
admin.site.site_title = 'ПКИПТ API'