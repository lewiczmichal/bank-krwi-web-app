# Generated by Django 3.0.7 on 2020-06-17 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sqlserver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grupakrwi', models.CharField(max_length=5)),
                ('rh', models.CharField(max_length=5)),
            ],
        ),
    ]
