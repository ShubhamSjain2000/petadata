import uuid

from django.db import models

from core.models import TimeStampMixin
from auth_management.models import User


class WorkSpace(models.Model):

    workspace_id = models.UUIDField(primary_key=True, default=uuid.uuid4())
    created_by = models.ForeignKey(User, null=False, on_delete=models.CASCADE, related_name='created_by')
    name = models.CharField(max_length=100, blank=False, null=False, unique=True)
    participants = models.ManyToManyField(User)

    def __str__(self):
        return self.name


class WorkFlow(TimeStampMixin):
    workflow_id = models.UUIDField(primary_key=True, default=uuid.uuid4())
    name = models.CharField(max_length=100, blank=False, null=False)
    created_by = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    workspace_id = models.ForeignKey(WorkSpace, null=False, on_delete=models.CASCADE,
                                     related_name='workflows')

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['workspace_id', 'name'],
                name='unique_workspace_name'
            )
        ]

    def __str__(self):
        return self.name


class WorkFlowTrigger(models.Model):
    class Status(models.TextChoices):

        STARTED = "STARTED"
        SUCCESS = "SUCCESS"
        FAILED = "FAILED"

    workflow_trigger_id = models.UUIDField(primary_key=True, default=uuid.uuid4())
    workflow_id = models.ForeignKey(WorkFlow, null=False, on_delete=models.CASCADE,
                                    related_name='workflow_triggers')
    triggered_by = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    started_at = models.DateTimeField(auto_now_add=True)
    ended_at = models.DateTimeField(null=True)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.STARTED)







