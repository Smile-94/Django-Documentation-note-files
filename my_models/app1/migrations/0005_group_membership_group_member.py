# Generated by Django 4.1.3 on 2022-12-03 21:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_runner'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_joinded', models.DateField()),
                ('invite_reason', models.CharField(max_length=100)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.group')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.person')),
            ],
        ),
        migrations.AddField(
            model_name='group',
            name='member',
            field=models.ManyToManyField(through='app1.Membership', to='app1.person'),
        ),
    ]