# Generated by Django 4.2.6 on 2023-10-13 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('terhal', '0003_alter_hotel_hotel_rating'),
        ('recommendation', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recommendation',
            name='category',
        ),
        migrations.AddField(
            model_name='recommendation',
            name='category',
            field=models.ManyToManyField(to='terhal.category', verbose_name='Category'),
        ),
    ]
