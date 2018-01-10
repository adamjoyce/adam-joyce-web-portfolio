from django.shortcuts import render

from .models import Project

def projects(request):
    context_dict = {}

    # All Projects.
    projects = Project.objects.all()
    context_dict['projects'] = projects

    # Get all project dates for sorting purposesself.
    dates = []
    for project in projects:
        year = project.get_year()
        if year not in dates:
            dates.append(year)
    context_dict['dates'] = dates        

    return render (request, 'projects/projects.html', context_dict);
