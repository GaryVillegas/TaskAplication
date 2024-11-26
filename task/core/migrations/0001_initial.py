# Generated by Django 5.1.1 on 2024-11-26 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, help_text='Enter a task title', max_length=100, null=True)),
                ('time_task', models.DateField(help_text='how long it will take you to finish')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('desciption', models.TextField(blank=True, help_text='Enter your task here', max_length=500, null=True)),
            ],
        ),
    ]
