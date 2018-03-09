from django.shortcuts import render

from .models import Category, Project

def projects(request, active_filter=None):
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

    # Sort projects depending on active filter.
    if active_filter:
        for cat in categories:
            if active_filter.title() == cat.name:
                projects = Project.objects.filter(
                    categories__name__iexact=active_filter.title()).order_by(
                    '-date')
                break
        else:
            # Active filter is a year date.
            active_filter = int(active_filter)
            projects = Project.objects.filter(
                date__year=active_filter).order_by('-date')
        context_dict['active_filter'] = active_filter

    context_dict['projects'] = projects

    return render (request, 'projects/projects.html', context_dict)
