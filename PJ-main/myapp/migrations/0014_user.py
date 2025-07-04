# Generated by Django 4.2.23 on 2025-06-14 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0013_alter_order_user_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(blank=True, max_length=255, null=True)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('membership', models.BooleanField(default=False)),
                ('email', models.EmailField(blank=True, max_length=255, null=True)),
                ('createdAt', models.DateTimeField(auto_now_add=True, null=True)),
                ('updatedAt', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]
