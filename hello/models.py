from django.db import models

# Create your models here.
class Film(models.Model):
    title = models.CharField(max_length=64, blank=False, unique=True)
    year = models.PositiveSmallIntegerField(default=2000)
    models = models.TextField(default="")
    premiere = models.DateField(null=True, blank=True)
    imbd_rating = models.DecimalField(max_digit=4, decimal_places=2, null=True, blank=True)
    poster = models.ImageField(upload_to="posters", null=True, blank=True)

    def __str__(self):
        return self.title_with_year()

    def title_with_year(self):
        return "{} ({})".format(self.title, self.year)