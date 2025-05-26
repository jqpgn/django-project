from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class EducationProgram(models.Model):
    PROGRAM_TYPES = [
        ('B', 'Бакалавриат'),
        ('M', 'Магистратура'),
        ('S', 'Аспирантура'),
        ('AD', 'ДПО'),
    ]

    name = models.CharField(max_length=200, verbose_name="Название профиля")
    program_type = models.CharField(
        max_length=2, choices=PROGRAM_TYPES, verbose_name="Тип профиля")
    duration = models.PositiveSmallIntegerField(
        verbose_name="Длительность (лет)")
    start_date = models.DateField(verbose_name="Дата начала")
    is_active = models.BooleanField(default=True, verbose_name="Активна")
    description = models.TextField(blank=True, verbose_name="Описание")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = "Профили"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.get_program_type_display()}: {self.name}"
