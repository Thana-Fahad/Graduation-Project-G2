# Generated by Django 4.2.6 on 2023-10-21 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recommendation', '0006_alter_recommendation_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recommendation',
            name='canonical',
            field=models.URLField(blank=True, max_length=255, null=True, verbose_name='Canonical'),
        ),
    ]