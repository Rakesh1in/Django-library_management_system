# Generated by Django 5.0 on 2024-09-04 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='year',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='student',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='student_class',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]