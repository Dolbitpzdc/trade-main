# Generated by Django 3.1.3 on 2021-01-16 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firms', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Add_employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Register_a_company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.TextField()),
            ],
        ),
    ]
