from rest_framework import serializers
from .models import EnrolleeSpeciality


class EnrolleeSpecialitySerializer(serializers.ModelSerializer):
    class Meta:
        model = EnrolleeSpeciality
        fields = ['enrollee_snils', 'speciality_name', 'priority', 'is_enrolled']
