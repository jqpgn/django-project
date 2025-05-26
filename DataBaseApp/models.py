from django.db import models
from django.urls import reverse


class Page(models.Model):
    title = models.CharField('Название страницы', max_length=100)
    slug = models.SlugField('URL', unique=True)
    order = models.PositiveIntegerField('Порядок', default=0)

    class Meta:
        ordering = ['order']
        verbose_name = 'Страница'
        verbose_name_plural = 'Страницы'

    def __str__(self):
        return self.title


class StudentProfile(models.Model):
    page = models.OneToOneField(
        Page, on_delete=models.CASCADE, related_name='student_profile')
    full_name = models.CharField('ФИО', max_length=100)
    photo = models.FileField('Фото', upload_to='students/')
    email = models.EmailField('Email')
    phone = models.CharField('Телефон', max_length=20)
    resume = models.TextField('Резюме')
    portfolio_link = models.URLField('Ссылка на портфолио', blank=True)


class ProgramInfo(models.Model):
    page = models.OneToOneField(
        Page, on_delete=models.CASCADE, related_name='program_info')
    title = models.CharField('Название ОП', max_length=200)
    program_link = models.URLField('Ссылка на ОП')
    curriculum = models.TextField('Что я буду изучать')
    skills = models.TextField('Чему научусь')
    advantages = models.TextField('Преимущества программы')
    prospects = models.TextField('Перспективы после обучения')


class Manager(models.Model):
    ROLE_CHOICES = [
        ('academic', 'Академический руководитель'),
        ('manager', 'Менеджер программы'),
    ]
    page = models.ForeignKey(
        Page, on_delete=models.CASCADE, related_name='managers')
    full_name = models.CharField('ФИО', max_length=100)
    photo = models.FileField('Фото', upload_to='managers/')
    email = models.EmailField('Email')
    role = models.CharField('Роль', max_length=20, choices=ROLE_CHOICES)


class Classmate(models.Model):
    page = models.ForeignKey(
        Page, on_delete=models.CASCADE, related_name='classmates')
    full_name = models.CharField('ФИО', max_length=100)
    photo = models.FileField('Фото', upload_to='classmates/')
    email = models.EmailField('Email')
    phone = models.CharField('Телефон', max_length=20, blank=True)
