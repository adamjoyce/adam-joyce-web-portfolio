from django.shortcuts import render

from .models import Category, Project

def projects(request, active_category=None, active_year=None):
    context_dict = {}

    # Get all categories for filtering.
    categories = Category.objects.all().order_by('name')
    context_dict['categories'] = categories

    # Get all project dates for filtering.
    dates = []
    projects = Project.objects.all().order_by('-date')
    for project in projects:
        year = project.get_year()
        if year not in dates:
            dates.append(year)
    context_dict['dates'] = dates

    print(active_year)

    # Sort projects depending on active filter.
    if active_category:
        projects = Project.objects.filter(
            categories__name__iexact=active_category).order_by('-date')
    elif active_year:
        active_year = int(active_year)
        print('WORKING')
        projects = Project.objects.filter(
            date__year=active_year).order_by('-date')

    context_dict['active_category'] = active_category
    context_dict['active_year'] = active_year
    context_dict['projects'] = projects

    return render (request, 'projects/projects.html', context_dict);
