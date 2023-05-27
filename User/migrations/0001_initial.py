# Generated by Django 4.2 on 2023-05-27 11:13

import User.manager
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
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
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('objects', User.manager.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='SimpleUser',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('lastname', models.CharField(max_length=30)),
            ],
            options={
                'abstract': False,
            },
            bases=('User.user',),
            managers=[
                ('objects', User.manager.UserManager()),
            ],
        ),
    ]
