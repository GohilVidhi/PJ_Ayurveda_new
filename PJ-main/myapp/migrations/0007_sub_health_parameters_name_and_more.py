# Generated by Django 4.2.23 on 2025-06-14 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_sub_health_parameters'),
    ]

    operations = [
        migrations.CreateModel(
            name='sub_health_parameters_name',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parameter_name', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='sub_health_parameters',
            name='sub_parameter_name',
        ),
        migrations.AddField(
            model_name='sub_health_parameters',
            name='sub_parameter_name',
            field=models.ManyToManyField(to='myapp.sub_health_parameters_name'),
        ),
    ]
