# Generated by Django 3.2 on 2023-07-31 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workers', '0002_remove_worker_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worker',
            name='status',
            field=models.CharField(choices=[('FREE', 'Free'), ('OCCUPIED', 'Occupied')], db_index=True, default='FREE', max_length=50),
        ),
    ]
