from . import serializers, use_cases
from rest_framework.response import Response
from .exc import *
from django.http import *
from rest_framework.views import APIView
from . import responses
from . import exc


class RecruitmentAPIView(APIView):
    def get(self, request):  
        recruitments = serializers.RecruimentSerializer(
            use_cases.get_recruitments(),
            many=True,
        )

        return Response(recruitments.data)


class EnrolleeAPIView(APIView):
    def get(self, request, snils):
        try:
            enrollee = serializers.EnrolleeSerializer(
                use_cases.get_enrollee(snils)
            )
            return Response(enrollee.data)
        except(exc.EnrolleeNotFound):
            raise responses.EnrolleNotFound()
        except(exc.EnrolleeDoesNotHavePrioritySpeciality):
            raise responses.EnrolleeDoesNotHavePrioritySpeciality()


class SpecialityAPIView(APIView):
    def get(self, request):  
        specialities = serializers.SpecialitySerializer(
            use_cases.get_specialities(),
            many=True,
        )

        return Response(specialities.data)