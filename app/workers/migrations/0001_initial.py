# Generated by Django 3.2 on 2023-07-16 20:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('educations', '0001_initial'),
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=50)),
                ('last_name', models.CharField(blank=True, max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('level', models.CharField(choices=[('JUNIOR', 'Junior'), ('MID', 'Mid'), ('SENIOR', 'Senior')], db_index=True, max_length=50)),
                ('status', models.CharField(choices=[('FREE', 'Free'), ('OCCUPIED', 'Occupied')], db_index=True, max_length=50)),
                ('categories', models.ManyToManyField(to='categories.Category')),
                ('education', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='educations.education')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]