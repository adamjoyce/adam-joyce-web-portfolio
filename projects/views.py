from django.shortcuts import render

from .models import FinancialCategory, TechnologyCategory, Project

# Project selection grid.
def projects(request, cat_filter=None):
    context_dict = {}

    # Setup the filter menu context dictionary entries.
    setup_filter_menu(context_dict)
    projects = context_dict['projects']
    financial_categories = context_dict['financial_categories']
    technology_categories = context_dict['technology_categories']
    dates = context_dict['dates']

    # Sort projects depending on the active category filter.
    if cat_filter:
        category_found = False
        cat_filter_titled = cat_filter.title()

        # Test to see if the category is a financial or technology category.
        if search_category(financial_categories, cat_filter_titled):
            projects = Project.objects.filter(
                financial_categories__name__iexact=
                    cat_filter.title()).order_by('-date')
            category_found = True
        elif search_category(technology_categories, cat_filter_titled):
            projects = Project.objects.filter(
                technology_categories__name__iexact=
                    cat_filter.title()).order_by('-date')
            category_found = True

        if not category_found:
            # Test to see if the category is a valid year date.
            if cat_filter.isdigit():
                cat_filter = int(cat_filter)
                if cat_filter in dates:
                    projects = Project.objects.filter(
                        date__year=cat_filter).order_by('-date')
                    category_found = True

        if not category_found:
            # Category is invalid.
            cat_filter = 'INVALID'

        context_dict['cat_filter'] = cat_filter

    context_dict['projects'] = projects

    return render(request, 'projects/projects.html', context_dict)

# Individual project pages.
def project_page(request, financial_cat, project):
    context_dict = {}
    context_dict['project'] = project;

    # Setup the filter menu context dictionary entries.
    setup_filter_menu(context_dict)

    return render(request, 'projects/project_page.html', context_dict)

# Determines what filter categories are needed in the filter menu and adds them
# to the given context dictionary.
def setup_filter_menu(context_dict):
    # Get all financial and technology categories for filtering.
    financial_categories = FinancialCategory.objects.all().order_by('name')
    context_dict['financial_categories'] = financial_categories
    technology_categories = TechnologyCategory.objects.all().order_by('name')
    context_dict['technology_categories'] = technology_categories

    # Get all project year dates for filtering.
    dates = []
    projects = Project.objects.all().order_by('-date')
    for project in projects:
        year = project.get_year()
        if year not in dates:
            dates.append(year)
    context_dict['projects'] = projects
    context_dict['dates'] = dates

# Searches the given list for the given name.  Returns true if found.
def search_category(category_list, category_name):
    for cat in category_list:
        if cat.name == category_name:
            return True
    return False;
