from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.db.models import Prefetch

from .models import ProgramCategory, Program, Training, TrainingDate
from .forms import ProgramCategoryForm, ProgramForm, TrainingForm, TrainingDateForm

import calendar


# Create your views here.
def display_view(request):
    template_name = 'programme/display_view.html'
    months_to_view = 6
    current_month = 7

    month_array = [calendar.month_name[i+current_month][:3] for i in range(months_to_view)]

    program_cats = ProgramCategory.objects.all()\
            .prefetch_related(Prefetch('program__training__training_date', queryset=TrainingDate.objects.order_by('start_date')))

    return render(request, template_name, {'program_categories': program_cats, 'months' : month_array})

def all_edit(request):
    template_name = 'programme/all_edit.html'

    program_cats = ProgramCategory.objects.all() \
        .prefetch_related(
        Prefetch('program__training__training_date', queryset=TrainingDate.objects.order_by('start_date')))

    return render(request, template_name, {'program_categories': program_cats})

############### Program Category ###################
def program_category(request):
    template_name = 'programme/program_cat.html'

    program_cats = ProgramCategory.objects.all()

    return render(request, template_name, {'program_categories': program_cats})

def add_program_category(request):
    template_name = 'programme/program_cat_edit.html'

    if request.method == 'POST':
        forms = ProgramCategoryForm(request.POST)
        if forms.is_valid():
            forms.save()
            # do something.
            return HttpResponseRedirect(reverse('program_cat'))
    else:
        forms = ProgramCategoryForm()

    return render(request, template_name, {'forms': forms})

def edit_program_category(request, id):
    template_name = 'programme/program_cat_edit.html'

    program_cat = ProgramCategory.objects.get(pk=id)
    if request.method == 'GET':
        forms = ProgramCategoryForm(instance=program_cat)
        return render(request, template_name, {'forms': forms})
    elif request.method == 'POST':
        if request.POST.get('delete'):
            program_cat.delete()
            return HttpResponseRedirect(reverse('all_edit'))
        forms = ProgramCategoryForm(request.POST,instance=program_cat)
        if forms.is_valid():
            forms.save()
            # do something.
            return HttpResponseRedirect(reverse('all_edit'))

############### Program ###################
def program(request):
    template_name = 'programme/program.html'

    program = Program.objects.select_related('category').all()

    return render(request, template_name, {'programs': program})

def program_add(request):
    template_name = 'programme/program_edit.html'

    if request.method == 'GET':
        forms = ProgramForm()
        return render(request, template_name, {'forms': forms})
    elif request.method == 'POST':
        forms = ProgramForm(request.POST)
        if forms.is_valid():
            forms.save()
            # do something.
            return HttpResponseRedirect(reverse('program'))

    return render(request, template_name, {'forms' : forms})

def program_edit(request, id):
    template_name = 'programme/program_edit.html'

    program = Program.objects.get(pk=id)
    if request.method == 'GET':
        forms = ProgramForm(instance=program)
        return render(request, template_name, {'forms': forms})
    elif request.method == 'POST':
        if request.POST.get('delete'):
            program.delete()
            return HttpResponseRedirect(reverse('all_edit'))
        forms = ProgramForm(request.POST,instance=program)
        if forms.is_valid():
            forms.save()
            # do something.
            return HttpResponseRedirect(reverse('all_edit'))

    return render(request, template_name, {'forms' : forms})

############### Training ###################
def training(request):
    template_name = 'programme/training.html'

    program_cats = ProgramCategory.objects.all()
    return render(request, template_name, {'program_categories': program_cats})

def training_add(request):
    template_name = 'programme/training_edit.html'

    if request.method == 'GET':
        forms = TrainingForm()
        return render(request, template_name, {'forms': forms})
    elif request.method == 'POST':
        forms = TrainingForm(request.POST, request.FILES)
        if forms.is_valid():
            forms.save()
            # do something.
            return HttpResponseRedirect(reverse('training'))

    return render(request, template_name, {'forms': forms})

def training_edit(request, id):
    template_name = 'programme/training_edit.html'

    training = Training.objects.get(pk=id)
    if request.method == 'GET':
        forms = TrainingForm(instance=training)
        return render(request, template_name, {'forms': forms})
    elif request.method == 'POST':
        if request.POST.get('delete'):
            training.delete()
            return HttpResponseRedirect(reverse('all_edit'))
        forms = TrainingForm(request.POST, request.FILES, instance=training)
        if forms.is_valid():
            forms.save()
            # do something.
            return HttpResponseRedirect(reverse('all_edit'))

    return render(request, template_name, {'forms': forms})

############### Training Date ###################

def training_date(request):
    template_name = 'programme/training_date.html'

    program_cats = ProgramCategory.objects.all() \
        .prefetch_related(
        Prefetch('program__training__training_date', queryset=TrainingDate.objects.order_by('start_date')))

    return render(request, template_name, {'program_categories': program_cats})

def training_date_add(request):
        template_name = 'programme/training_date_edit.html'

        if request.method == 'GET':
            forms = TrainingDateForm()
            return render(request, template_name, {'forms': forms})
        elif request.method == 'POST':
            forms = TrainingDateForm(request.POST)
            if forms.is_valid():
                forms.save()
                # do something.
                return HttpResponseRedirect(reverse('training_date'))

        return render(request, template_name, {'forms': forms})

def training_date_edit(request, id):
    template_name = 'programme/training_date_edit.html'

    training_date = TrainingDate.objects.get(pk=id)
    if request.method == 'GET':
        forms = TrainingDateForm(instance=training_date)
        return render(request, template_name, {'forms': forms})
    elif request.method == 'POST':
        if request.POST.get('delete'):
            training_date.delete()
            return HttpResponseRedirect(reverse('all_edit'))
        forms = TrainingDateForm(request.POST, instance=training_date)
        if forms.is_valid():
            forms.save()
            # do something.
            return HttpResponseRedirect(reverse('all_edit'))

    return render(request, template_name, {'forms': forms})