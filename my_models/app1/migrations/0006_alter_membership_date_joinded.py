# Generated by Django 4.1.3 on 2022-12-03 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_group_membership_group_member'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membership',
            name='date_joinded',
            field=models.DateField(auto_now_add=True),
        ),
    ]
