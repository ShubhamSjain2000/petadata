from django.dispatch import receiver
from django.db.models.signals import pre_save
from django.shortcuts import get_object_or_404

from workflow.models import WorkSpace
from workflow.tasks import async_send_mail


@receiver(pre_save, sender=WorkSpace)
def get_notified_for_workspace_update(sender, instance, **kwargs):

    try:
        previous_obj = get_object_or_404(sender, pk=instance.pk)
        if previous_obj.name == instance.name:
            return
        subject = "WorkSpace Updated"
        body = f"WorkSpace name updated from {previous_obj.name} to {instance.name}"
        emails = list(previous_obj.participants.values_list('email', flat=True))
        async_send_mail.delay(subject, body, emails)
    except Exception as e:
        return
