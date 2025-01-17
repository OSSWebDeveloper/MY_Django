# Generated by Django 5.0.6 on 2024-07-05 05:54

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=255, verbose_name='Sarlavha')),
                ('description', models.TextField(blank=True, db_index=True, verbose_name='Izoh')),
                ('image', models.ImageField(db_index=True, upload_to='', verbose_name='Rasm')),
                ('date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Sana')),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Postlar',
            },
        ),
    ]
