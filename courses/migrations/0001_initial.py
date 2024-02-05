# Generated by Django 4.2.9 on 2024-02-04 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('instructor', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'course_data',
            },
        ),
    ]
