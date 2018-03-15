from django.db import models
from django.utils import timezone
from django.template.defaultfilters import slugify

class Category(models.Model):
    name = models.CharField(max_length=25, unique=True)
    slug = models.SlugField(unique=True, blank=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class FinancialCategory(Category):
    class Meta:
        verbose_name_plural = 'FinancialCategories'

class TechnologyCategory(Category):
    class Meta:
        verbose_name_plural = 'TechnologyCategories'

class Project(models.Model):
    financial_categories = models.ForeignKey(FinancialCategory,
                                             on_delete=models.CASCADE)
    technology_categories = models.ManyToManyField(TechnologyCategory)
    title = models.CharField(max_length=25, unique=True)
    date = models.DateTimeField(default=timezone.now)
    summary = models.CharField(max_length=100, default='Project summary.',
                               help_text='A short summary of the project.')
    description = models.TextField()
    logo = models.ImageField(upload_to='projects/project_logos', blank=True)
    color = models.TextField(blank=True,
                             help_text='Background color for project overlay.')
    link = models.URLField()
    image = models.ImageField(upload_to='projects/project_images', blank=True,
                              help_text='Site image for project page.')
    slug = models.SlugField(unique=True, blank=True)

    def get_logo(self):
        if self.logo and hasattr(self.logo, 'url'):
            return self.logo.url
        else:
            return '/static/images/default_logo.jpg'

    def get_image(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
        else:
            return '/static/images/default_image.jpg'

    def get_year(self):
        return self.date.year;

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Project, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
