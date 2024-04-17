from . import serializers, use_cases
from rest_framework.response import Response
from .exc import *
from django.http import *
from rest_framework.views import APIView


class RecruitmentAPIView(APIView):
    def get(self, request):  
        recruitments = serializers.RecruimentSerializer(
            use_cases.get_recruitments(),
            many=True,
        )

        return Response(recruitments.data)


class EnrolleeAPIView(APIView):
    def get(self, request, snils):
        enrollee = serializers.EnrolleeSerializer(
            use_cases.get_enrollee(snils)
        )

        return Response(enrollee.data)
