# Generated by Django 4.1.3 on 2022-12-02 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app2', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='num_stars',
            field=models.IntegerField(choices=[(1, 'Poor'), (2, 'Bad'), (3, 'Average'), (4, 'Good'), (5, 'Excellent')]),
        ),
    ]
