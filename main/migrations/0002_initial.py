# Generated by Django 4.2.11 on 2024-06-25 07:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='messagemodel',
            name='email',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='emails', to=settings.AUTH_USER_MODEL, verbose_name='Email'),
        ),
        migrations.AddField(
            model_name='messagemodel',
            name='user_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='users_name', to=settings.AUTH_USER_MODEL, verbose_name='Username'),
        ),
    ]
