# Generated by Django 2.2.4 on 2019-09-01 21:31

import core.models.validators.json_schema_validator
import django.contrib.postgres.fields.jsonb
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20190827_2039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='table',
            name='big_blind',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='table',
            name='small_blind',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.CreateModel(
            name='Hand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('history', django.contrib.postgres.fields.jsonb.JSONField(validators=[core.models.validators.json_schema_validator.JsonSchemaValidator('hand_history_schema')])),
                ('table', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.Table')),
            ],
        ),
    ]
