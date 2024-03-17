from datetime import datetime

from rest_framework import status
from rest_framework.test import APITestCase
from .models import *

class ApiTestCase(APITestCase):
    def test_get_enrollee_raiting(self):
        current = Current.objects.create(
            is_open=True,
            year=2024,
            number=1,
        )

        enrollee = Enrollee.objects.create(
            full_name='',
            snils='snils1',
            inn='inn',
            gpa=4.8,
            application_date=datetime.now().date(),
            current_id=current,
        )

        speciality = Speciality.objects.create(
            name = 'Программист',
            seats_amount=25,
        )

        EnrolleeSpeciality.objects.create(
            enrollee_snils=enrollee,
            speciality_name=speciality,
            priority=1,
            is_enrolled=False,
        )

        response = self.client.get(f'/api/enrollee/{enrollee.snils}/rating')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['data']['rating'], 1)

    def test_get_enrollee_specialitis(self):
        current = Current.objects.create(
            is_open=True,
            year=2024,
            number=1,
        )

        enrollee = Enrollee.objects.create(
            full_name='',
            snils='snils1',
            inn='inn',
            gpa=4.8,
            application_date=datetime.now().date(),
            current_id=current,
        )

        speciality = Speciality.objects.create(
            name = 'Программист',
            seats_amount=25,
        )

        speciality_2 = Speciality.objects.create(
            name = 'Системный Администратор',
            seats_amount=25,
        )

        speciality_3 = Speciality.objects.create(
            name = 'Безопастность',
            seats_amount=25,
        )

        EnrolleeSpeciality.objects.create(
            enrollee_snils=enrollee,
            speciality_name=speciality,
            priority=1,
            is_enrolled=False,
        )

        EnrolleeSpeciality.objects.create(
            enrollee_snils=enrollee,
            speciality_name=speciality_2,
            priority=2,
            is_enrolled=False,
        )

        EnrolleeSpeciality.objects.create(
            enrollee_snils=enrollee,
            speciality_name=speciality_3,
            priority=2,
            is_enrolled=False,
        )

        response = self.client.get(f'/api/enrollee/{enrollee.snils}/rating')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
