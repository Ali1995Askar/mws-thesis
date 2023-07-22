# Generated by Django 3.2 on 2023-07-22 22:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('categories', '0001_initial'),
        ('educations', '0001_initial'),
        ('workers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('deadline', models.DateField()),
                ('level', models.CharField(choices=[('JUNIOR', 'Junior'), ('MID', 'Mid'), ('SENIOR', 'Senior')], db_index=True, max_length=50)),
                ('status', models.CharField(choices=[('OPEN', 'Open'), ('DONE', 'Done'), ('PROGRESS', 'Progress')], db_index=True, max_length=50)),
                ('created_on_datetime', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_on_datetime', models.DateTimeField(auto_now=True, db_index=True)),
                ('assigned_to', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='workers.worker')),
                ('categories', models.ManyToManyField(to='categories.Category')),
                ('educations', models.ManyToManyField(to='educations.Education')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
