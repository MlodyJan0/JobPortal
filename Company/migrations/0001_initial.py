# Generated by Django 4.2 on 2023-05-21 15:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='User.user')),
                ('nip', models.DecimalField(decimal_places=0, max_digits=10, unique=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('User.user',),
        ),
    ]
