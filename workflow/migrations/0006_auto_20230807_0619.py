# Generated by Django 3.2 on 2023-08-07 06:19

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('workflow', '0005_auto_20230806_1522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workflow',
            name='workflow_id',
            field=models.UUIDField(default=uuid.UUID('0e8edece-2c12-4f57-bb14-eda4988de2e3'), primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='workflowtrigger',
            name='workflow_trigger_id',
            field=models.UUIDField(default=uuid.UUID('627e21f5-b83d-42ca-85f3-f80f97be4006'), primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='workspace',
            name='workspace_id',
            field=models.UUIDField(default=uuid.UUID('697b91e8-2d41-47b5-b4c1-505d79f9cdc7'), primary_key=True, serialize=False),
        ),
    ]
