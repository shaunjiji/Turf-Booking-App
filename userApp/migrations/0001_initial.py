# Generated by Django 4.1.5 on 2023-02-01 08:10

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('adminApp', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bookingdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.CharField(choices=[('3 PM', '3 PM'), ('3:30 PM', '3:30 PM'), ('4 PM', '4 PM'), ('4:30 PM', '4:30 PM'), ('5 PM', '5 PM'), ('5:30 PM', '5:30 PM'), ('6 PM', '6 PM'), ('6:30 PM', '6:30 PM'), ('7 PM', '7 PM'), ('7:30 PM', '7:30 PM'), ('8:00 PM', '8:00 PM'), ('8:30 PM', '8:30 PM'), ('9:00 PM', '9:00 PM'), ('9:30 PM', '9:30 PM'), ('10:00 PM', '10:00 PM'), ('10:30 PM', '10:30 PM'), ('11:00 PM', '11:00 PM')], max_length=100)),
                ('time_booked', models.DateTimeField(default=datetime.datetime.now)),
                ('status', models.CharField(choices=[(0, 'Pending'), (1, 'Approved')], default='Pending', max_length=100)),
                ('turfid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminApp.turfdb')),
                ('userid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
