from django.db.models import Avg
from django.views.generic import ListView
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from django.db.models import Count, Avg
from .models import EducationProgram
from .forms import EducationProgramForm
from django.http import HttpResponse


def index1(request):
    return HttpResponse("Привет из приложения 1!")


def program_create(request):
    if request.method == 'POST':
        form = EducationProgramForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('MyProgramApp:program_list')
    else:
        form = EducationProgramForm()
    return render(request, 'MyProgramApp/program_form.html', {'form': form})


class ProgramListView(ListView):
    model = EducationProgram
    template_name = 'MyProgramApp/program_list.html'
    context_object_name = 'programs'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()

        program_type = self.request.GET.get('program_type')
        is_active = self.request.GET.get('is_active')

        if program_type:
            queryset = queryset.filter(program_type=program_type)
        if is_active:
            queryset = queryset.filter(is_active=is_active == 'true')

        sort = self.request.GET.get('sort')
        if sort in ['name', '-name', 'start_date', '-start_date']:
            queryset = queryset.order_by(sort)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        type_stats = []
        for choice in EducationProgram.PROGRAM_TYPES:
            stats = EducationProgram.objects.filter(program_type=choice[0]).aggregate(
                count=Count('id'),
                avg_duration=Avg('duration')
            )
            type_stats.append({
                'program_type': choice[0],
                'type_display': choice[1],
                'count': stats['count'],
                'avg_duration': stats['avg_duration']
            })

        context['type_stats'] = type_stats

        context['stats'] = {
            'total': EducationProgram.objects.count(),
            'active': EducationProgram.objects.filter(is_active=True).count(),
            'avg_duration': EducationProgram.objects.aggregate(
                avg=Avg('duration')
            )['avg'],
            # 'short_programs': EducationProgram.objects.filter(duration__lt=4).count(),
            # 'name': EducationProgram.objects.filter(duration__lt=4).values_list('name', flat=True),
        }

        context['current_filters'] = {
            'program_type': self.request.GET.get('program_type', ''),
            'is_active': self.request.GET.get('is_active', ''),
            'sort': self.request.GET.get('sort', ''),
        }

        return context


def program_detail(request, pk):
    program = get_object_or_404(EducationProgram, pk=pk)
    return render(request, 'MyProgramApp/program_detail.html', {'program': program})


def program_update(request, pk):
    program = get_object_or_404(EducationProgram, pk=pk)
    if request.method == 'POST':
        form = EducationProgramForm(request.POST, instance=program)
        if form.is_valid():
            form.save()
            return redirect('MyProgramApp:program_detail', pk=program.pk)
    else:
        form = EducationProgramForm(instance=program)

    return render(request, 'MyProgramApp/program_form.html', {'form': form})


def program_delete(request, pk):
    program = get_object_or_404(EducationProgram, pk=pk)
    if request.method == 'POST':
        program.delete()
        return redirect('MyProgramApp:program_list')
    return render(request, 'MyProgramApp/program_confirm_delete.html', {'program': program})
