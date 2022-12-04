from django.db import models

# Create your models here.

class Musician(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    instrument=models.CharField(max_length=50)


nam_star_choose=[
    (1,'Poor'),
    (2,'Bad'),
    (3,'Average'),
    (4,'Good'),
    (5,'Excellent')
]

class Album(models.Model):
    artist=models.ForeignKey(Musician, on_delete=models.CASCADE, verbose_name='artist name')
    name=models.CharField('album names',max_length=50)
    release_date=models.DateField()
    num_stars=models.IntegerField(choices=nam_star_choose)
