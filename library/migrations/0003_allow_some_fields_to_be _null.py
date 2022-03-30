# Generated by Django 4.0.3 on 2022-03-30 16:39

import django.core.validators
from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_alter_borrow_date_to_datetime_field'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='birth_date',
            field=models.PositiveSmallIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='author',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='author',
            name='nationality',
            field=django_countries.fields.CountryField(max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='author',
            name='rating',
            field=models.DecimalField(decimal_places=2, max_digits=3, null=True, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(5.0)]),
        ),
        migrations.AlterField(
            model_name='book',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='rating',
            field=models.DecimalField(decimal_places=2, max_digits=3, null=True, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(5.0)]),
        ),
        migrations.AlterField(
            model_name='category',
            name='description',
            field=models.TextField(null=True),
        ),
    ]
