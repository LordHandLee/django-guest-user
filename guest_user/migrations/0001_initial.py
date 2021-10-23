# Generated by Django 3.2.8 on 2021-10-23 16:13

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Created at')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='guest+', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Guest',
                'verbose_name_plural': 'Guests',
                'swappable': 'GUEST_USER_MODEL',
            },
        ),
    ]
