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

class Project(models.Model):
    categories = models.ManyToManyField(Category)
    title = models.CharField(max_length=25, unique=True)
    date = models.DateTimeField(default=timezone.now)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/project_images', blank=True)
    color = models.TextField(blank=True,
                             help_text='Background color for project overlay.')
    slug = models.SlugField(unique=True, blank=True)

    def get_year(self):
        return self.date.year;

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Project, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
