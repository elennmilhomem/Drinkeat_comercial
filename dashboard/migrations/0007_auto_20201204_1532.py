# Generated by Django 3.1.2 on 2020-12-04 18:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dashboard', '0006_auto_20201204_1513'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='primeiro_nome',
            field=models.CharField(default=None, max_length=30),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
