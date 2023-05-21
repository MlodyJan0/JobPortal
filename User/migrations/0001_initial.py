# Generated by Django 4.2 on 2023-05-21 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('zipcode', models.CharField(max_length=5)),
                ('city', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=80)),
                ('phoneNumber', models.DecimalField(decimal_places=0, max_digits=9, null=True)),
                ('type', models.CharField(default='myuser', editable=False, max_length=10)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]