from django.shortcuts import render

from .models import Project

def projects(request, active_year=None):
    context_dict = {}

    # The filtered page by year - None = all projects.
    if active_year:
        active_year = int(active_year)
    context_dict['active_year'] = active_year

    # Get all project dates for sorting purposes.
    dates = []
    projects = Project.objects.all().order_by('-date')
    for project in projects:
        year = project.get_year()
        if year not in dates:
            dates.append(year)
    context_dict['dates'] = dates

    # Revelent projects dependent on active year.
    if active_year:
        projects = Project.objects.filter(
            date__year=active_year).order_by('-date')
    context_dict['projects'] = projects

    print(type(active_year))
    print(type(dates[0]))

    return render (request, 'projects/projects.html', context_dict);
