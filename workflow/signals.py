from django.db.models.signals import pre_save
from django.dispatch import receiver

from workflow.models import WorkSpace


@receiver(pre_save, sender=WorkSpace)
def get_notified(sender, instance, **kwargs):

    pk = instance.pk
    previous_obj = sender.objects.get(pk=instance.pk)
    if previous_obj.name == instance.name:
        pass
        print("x")
        return
    print("y")