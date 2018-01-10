from django.db import models
from django.utils import timezone
from django.template.defaultfilters import slugify

class Project(models.Model):
    title = models.CharField(max_length=25, unique=True)
    date = models.DateTimeField(default=timezone.now)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/project_images', blank=True)
    slug = models.SlugField(unique=True, blank=True)

    def get_year(self):
        return self.date.year;

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Project, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
