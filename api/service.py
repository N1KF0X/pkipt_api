from .models import *
from .exc import *
from django.core.exceptions import ObjectDoesNotExist


def get_selected_specialities_by_enrollee_snils(enrollee_snils: str):
    return EnrolleeSpeciality.objects.filter(
        enrollee_snils=enrollee_snils
    ).all()


def get_enrollee(enrollee_snils: str):
    try:
        return Enrollee.objects.get(snils=enrollee_snils)
    except ObjectDoesNotExist:
        raise EnrolleeNotFound()
    

def get_selected_specialitiy_by_enrollee_snils(
        enrollee_snils: str,
        priority: int = 1,
    ):
    return EnrolleeSpeciality.objects.filter(
        enrollee_snils=enrollee_snils,
        priority=priority,
    ).first()


def get_selected_specialities_by_speciality_name(
        speciality_name: str,
        priority: int = 1,
    ):
    return EnrolleeSpeciality.objects.filter(
        speciality_name=speciality_name,
        priority=priority,
    )


def calculate_rating(enrollee_snils: str, priority: int = 1):
    current_enrollee = get_enrollee(enrollee_snils)
    selected_speciality = get_selected_specialitiy_by_enrollee_snils(
        enrollee_snils=enrollee_snils, 
        priority=priority,
    )
    selected_specialities = get_selected_specialities_by_speciality_name(
        speciality_name=selected_speciality.speciality_name.name, 
        priority=priority,
    )
    enrollee_snils = [
        selected_speciality.enrollee_snils.snils
        for selected_speciality 
        in selected_specialities
    ]

    enrollees = Enrollee.objects.filter(
        current_id=current_enrollee.current_id,
        snils__in=enrollee_snils,
    ).order_by('-gpa', 'application_date')

    raiting = 0
    for enrollee in enrollees:
        raiting += 1
        if enrollee.snils == current_enrollee.snils:
            break         
    
    return raiting
