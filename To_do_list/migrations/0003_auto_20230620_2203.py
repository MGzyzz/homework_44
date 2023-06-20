# Generated by Django 3.2.7 on 2023-06-20 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('To_do_list', '0002_alter_task_date_of_completion'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='name',
            field=models.TextField(max_length=250, null=True, verbose_name='Имя'),
        ),
        migrations.AddField(
            model_name='task',
            name='start_date',
            field=models.DateField(blank=True, null=True, verbose_name='Начало даты'),
        ),
    ]
