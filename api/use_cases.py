import datetime
from . import models
from .exc import *
from django.core.exceptions import ObjectDoesNotExist


def get_recruitments():
    return models.Recruitment.objects.filter(
        closing_date__gt=datetime.datetime.now()
    )


def get_enrollee(enrollee_snils: str):
    try:
        return models.Enrollee.objects.get(snils=enrollee_snils)
    except ObjectDoesNotExist:
        raise EnrolleeNotFound()


def get_enrollees_by_recruitment_name(recruitment_name: str):
    return models.Enrollee.objects.filter(
        recruitment=models.Recruitment.objects
        .get(name=recruitment_name),
    ).order_by('-gpa', 'application_date')


def get_priority_speciality(enrollee_snils: str):
    return models.EnrolleeSpeciality.objects.filter(
        enrollee=enrollee_snils,
        is_priority=True,
    ).first()


def calculate_rating(enrollee_snils: str):
    current_enrollee = get_enrollee(enrollee_snils)

    selected_speciality = get_priority_speciality(enrollee_snils)

    selected_specialities = models.EnrolleeSpeciality.objects.filter(
        speciality=selected_speciality.speciality.name,
        is_priority=True,
    )

    enrollee_snils = [
        selected_speciality.enrollee.snils
        for selected_speciality 
        in selected_specialities
    ]

    enrollees =  models.Enrollee.objects.filter(
        recruitment=current_enrollee.recruitment,
        snils__in=enrollee_snils,
    ).order_by('-gpa', 'application_date')

    raiting = 0
    for enrollee in enrollees:
        raiting += 1
        if enrollee.snils == current_enrollee.snils:
            break         
    
    return raiting


def enroll_recruitment(recruitment_name: str):
    enrollees = get_enrollees_by_recruitment_name(
        models.Recruitment.objects.get(name=recruitment_name).name
    )

    for enrollee in enrollees:
        priotity_speciality = get_priority_speciality(enrollee.snils)
        
        if priotity_speciality is None:
            continue
        
        rating = calculate_rating(enrollee.snils)        
        if rating <= priotity_speciality.speciality.seats_amount:
            priotity_speciality.is_enrolled = True
        else:
            priotity_speciality.is_enrolled = False
        priotity_speciality.save()


def reset_enrollment(recruitment_name: str):
    enrollees = get_enrollees_by_recruitment_name(recruitment_name)

    enrollee_snils = [
        enrollee.snils
        for enrollee 
        in enrollees
    ]

    selected_specialities = (
        models.EnrolleeSpeciality.objects
        .filter(enrollee__in=enrollee_snils)
    )

    for selected_speciality in selected_specialities:
        selected_speciality.is_enrolled = False
        selected_speciality.save()
