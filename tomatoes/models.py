from django.db import models

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=100, null=True)
    critic_rating = models.SmallIntegerField(null=True)
    poster = models.URLField(null=True)
    mpaa_rating = models.CharField(max_length=10, null=True)
    runtime = models.CharField(max_length = 4, null=True) #integerfield does not work because when you check it, it is a string?? but it works for other people's projects
    year = models.PositiveSmallIntegerField(null=True)
    audience_score = models.PositiveSmallIntegerField(null=True)
    movie_id = models.IntegerField(null=True)


    def __unicode__(self):
        return self.title


class Favorites(models.Model):
    title = models.CharField(max_length = 100, null=True)
    poster = models.URLField()
    identifier = models.URLField()
