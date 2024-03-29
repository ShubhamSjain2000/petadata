# Generated by Django 3.2 on 2023-08-07 09:30

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('workflow', '0007_auto_20230807_0644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workflow',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='workflow',
            name='workflow_id',
            field=models.UUIDField(default=uuid.UUID('40798c34-eeed-4046-b8bc-9c8a19a391a3'), primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='workflowtrigger',
            name='workflow_trigger_id',
            field=models.UUIDField(default=uuid.UUID('7eb7ef33-e0d9-4e3c-bd66-c2f27d574c41'), primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='workspace',
            name='workspace_id',
            field=models.UUIDField(default=uuid.UUID('79120d35-3fc1-4fa2-ba52-65fcd5066411'), primary_key=True, serialize=False),
        ),
    ]
