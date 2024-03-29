# Generated by Django 2.1 on 2021-05-04 17:14

from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pharma', '0013_auto_20210504_1115'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='names',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=550), default=list, size=None),
        ),
        migrations.AddField(
            model_name='payment',
            name='quantity',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(blank=True), default=list, size=None),
        ),
        migrations.AddField(
            model_name='payment',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='payment', to=settings.AUTH_USER_MODEL),
        ),
    ]
