# Generated by Django 4.2.6 on 2023-10-13 06:45

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('terhal', '0003_alter_hotel_hotel_rating'),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recommendation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('code', models.CharField(max_length=255, verbose_name='Code')),
                ('address', models.CharField(max_length=255, verbose_name='Address')),
                ('canonical', models.URLField(max_length=255, verbose_name='Canonical')),
                ('reviews_num', models.IntegerField(default=0, verbose_name='Reviews Number')),
                ('reviews_rating', models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)], verbose_name='Reviews Rating')),
                ('top_feature', models.TextField(verbose_name='Top Feature')),
                ('images', models.JSONField(blank=True, default=dict, null=True, verbose_name='Images')),
                ('description', models.TextField(verbose_name='Description')),
                ('top_facilities', models.TextField(verbose_name='Top Facilities')),
                ('reviews', models.JSONField(blank=True, default=dict, null=True, verbose_name='Reviews')),
                ('latitude', models.FloatField(default=0, verbose_name='Latitude')),
                ('longitude', models.FloatField(default=0, verbose_name='Longitude')),
                ('trending', models.BooleanField(default=False, verbose_name='Trending')),
                ('babies', models.BooleanField(default=False, verbose_name='Babies')),
                ('children', models.BooleanField(default=False, verbose_name='Children')),
                ('adults', models.BooleanField(default=False, verbose_name='Adults')),
                ('heart', models.BooleanField(default=False, verbose_name='Heart')),
                ('asthma', models.BooleanField(default=False, verbose_name='Asthma')),
                ('no_condition', models.BooleanField(default=False, verbose_name='No Condition')),
                ('stroller', models.BooleanField(default=False, verbose_name='Stroller')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='terhal.category', verbose_name='Category')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.city', verbose_name='City')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.country', verbose_name='Country')),
                ('hotels', models.ManyToManyField(to='terhal.hotel', verbose_name='Hotels')),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.state', verbose_name='State')),
            ],
        ),
        migrations.CreateModel(
            name='RecommendationImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='recommendations/images/', verbose_name='Image')),
                ('primary', models.BooleanField(default=False, verbose_name='Primary')),
                ('is_thumbnail', models.BooleanField(default=False, verbose_name='Is Thumbnail')),
                ('is_cover', models.BooleanField(default=False, verbose_name='Is Cover')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is Active')),
                ('recommendation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recommendation.recommendation', verbose_name='Recommendation')),
            ],
        ),
    ]
