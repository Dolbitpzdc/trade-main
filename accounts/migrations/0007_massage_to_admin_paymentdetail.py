# Generated by Django 3.1.7 on 2021-03-06 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_reviews'),
    ]

    operations = [
        migrations.CreateModel(
            name='Massage_to_admin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('massage', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='PaymentDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('free', models.TextField()),
                ('pro', models.TextField()),
                ('vip', models.TextField()),
            ],
        ),
    ]
