from django.contrib import admin
from .models import Page, StudentProfile, ProgramInfo, Manager, Classmate


class StudentProfileInline(admin.StackedInline):
    model = StudentProfile
    fields = ('full_name', 'photo', 'email',
              'phone', 'resume', 'portfolio_link')


class ProgramInfoInline(admin.StackedInline):
    model = ProgramInfo


class ManagerInline(admin.TabularInline):
    model = Manager
    extra = 1


class ClassmateInline(admin.TabularInline):
    model = Classmate
    extra = 2


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'order')
    list_editable = ('order',)
    prepopulated_fields = {'slug': ('title',)}
    inlines = [StudentProfileInline, ProgramInfoInline,
               ManagerInline, ClassmateInline]
