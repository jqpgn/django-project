from .models import Manager, Page
from .models import Manager
from django.shortcuts import render, get_object_or_404
from .models import Page
from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse


def page_detail(request, slug):
    page = get_object_or_404(Page, slug=slug)
    all_pages = Page.objects.all().order_by('order')
    return render(request, 'DataBaseApp/page.html', {
        'page': page,
        'all_pages': all_pages
    })


def classmates_list(request):
    classmates_page = get_object_or_404(Page, slug='students')
    classmates = classmates_page.classmates.all()
    all_pages = Page.objects.all().order_by('order')

    search_query = request.GET.get('search')
    if search_query:
        classmates = classmates.filter(full_name__icontains=search_query)

    sort = request.GET.get('sort', 'full_name')
    if sort in ['full_name', '-full_name', 'email', '-email']:
        classmates = classmates.order_by(sort)

    return render(request, 'DataBaseApp/classmates.html', {
        'classmates': classmates,
        'all_pages': all_pages,
        'search_query': search_query or '',
        'sort': sort
    })


def management_view(request):
    academic = Manager.objects.filter(role='academic').first()
    other_managers = Manager.objects.filter(role='manager')

    return render(request, 'DataBaseApp/management.html', {
        'academic': academic,
        'other_managers': other_managers,
        'all_pages': Page.objects.all(),
        'page': Page.objects.get(slug='management')
    })
