# Generated by Django 3.1.5 on 2021-01-19 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactsMacapa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('cellphone', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='ContactsVarejao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('cellphone', models.CharField(max_length=13)),
            ],
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
    ]
