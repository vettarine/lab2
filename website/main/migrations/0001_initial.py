# Generated by Django 3.2.23 on 2023-11-28 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SortedArray',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('array_name', models.CharField(max_length=100)),
                ('array', models.TextField()),
                ('sorted_array', models.TextField()),
            ],
        ),
    ]