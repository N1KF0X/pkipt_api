from django.db import models
from datetime import date

PRIORITY_CHOICES = (
    ('1', 1),
    ('2', 2),
    ('3', 3),
)


class Current(models.Model):
    number = models.IntegerField(verbose_name='Номер')
    is_open = models.BooleanField(verbose_name='Открыт')
    year = models.IntegerField(verbose_name='Год')

    def __str__(self):
        return f'{self.year} - {self.number}'

    class Meta:
        verbose_name = 'Поток'
        verbose_name_plural = 'Потоки'
        ordering = ['number', 'year']


class Enrollee(models.Model):
    full_name = models.CharField(max_length=50, verbose_name='ФИО')
    snils = models.CharField(primary_key=True, max_length=14, verbose_name='СНИЛС')
    inn = models.CharField(max_length=12, verbose_name='ИНН')
    gpa = models.FloatField(verbose_name='Средний Балл')
    application_date = models.DateField(null=True, verbose_name='Дата Подачи Документов')
    current_id = models.ForeignKey(
        Current, 
        on_delete = models.CASCADE, 
        verbose_name='Поток',
        null=True,
    )

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Абитуриент'
        verbose_name_plural = 'Абитуриенты'
        ordering = ['full_name', 'inn', 'gpa', 'current_id', 'application_date']


class Speciality(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название', primary_key=True)
    seats_amount = models.IntegerField(verbose_name='Количество Мест', default=25)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Специальность'
        verbose_name_plural = 'Специальности'
        ordering = ['name']


class EnrolleeSpeciality(models.Model):
    enrollee_snils = models.ForeignKey(
        Enrollee, 
        on_delete = models.CASCADE, 
        verbose_name='Абитуриент'
    )
    speciality_name = models.ForeignKey(
        Speciality, 
        on_delete = models.CASCADE, 
        verbose_name='Специальность'
    )
    priority = models.CharField(
        max_length=1, 
        choices=PRIORITY_CHOICES, 
        default='3',
        verbose_name='Приоритет'
    )
    is_enrolled = models.BooleanField(verbose_name='Зачислен', default=False)

    class Meta:
        verbose_name = 'Выбранная специальность'
        verbose_name_plural = 'Выбранные специальности'
        ordering = ['enrollee_snils', 'priority']

    def __str__(self):
        return f'{self.id}'
