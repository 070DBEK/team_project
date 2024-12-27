# Generated by Django 5.1.4 on 2024-12-27 16:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('teachers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('students', models.TextField()),
                ('teacher', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='teachers.teacher')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
