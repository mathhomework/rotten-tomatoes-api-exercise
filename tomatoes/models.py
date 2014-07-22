from django.db import models

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=100)
    release_year = models.PositiveSmallIntegerField()
    critic_rating = models.PositiveSmallIntegerField()
    poster = models.URLField()
    mpaa_rating = models.CharField(max_length=10, null=True)
    runtime = models.PositiveSmallIntegerField(null=True)
    year = models.PositiveSmallIntegerField(null=True)
    audience_score = models.PositiveSmallIntegerField(null=True)


    def __unicode__(self):
        return self.title