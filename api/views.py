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
        selected_specialities = serializers.SelectedSpecialitySerializer(
            use_cases.get_selected_specialities_by_enrollee_snils(snils),
            many=True,
        )

        enrollee = serializers.EnrolleeSerializer(
            use_cases.get_enrollee(snils)
        )

        return Response(enrollee.data)


# class EnrolleeSpeciality(APIView):
#     def get(self, request, snils):
#         selected_specialities = get_selected_specialities_by_enrollee_snils(snils)
#         serialized_selected_specialities = [
#             EnrolleeSpecialitySerializer(selected_speciality).data 
#             for selected_speciality in selected_specialities
#         ]
#         return Response({'data': serialized_selected_specialities})


# class RatingAPIView(APIView):
#     def get(self, request, snils):
#         try:
#             enrollee = get_enrollee(snils)
#             speciality = get_selected_specialitiy_by_enrollee_snils(snils)
#             rating = calculate_rating(snils)
#         except EnrolleeNotFound:
#             return HttpResponseNotFound('Абитуриент не найден.')
#         except EnrolleeSpecialityNotFound:
#             return HttpResponseBadRequest(content='Абитуриент не имеет приоритетную специальность.')

#         json = {
#             'data': {
#                 'full_name': enrollee.full_name,
#                 'speciality': speciality.speciality_name.name,
#                 'rating': rating,
#             }
#         }
#         return Response(json)