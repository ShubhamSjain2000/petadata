from django.db import models


class TimeStampMixin(models.Model):
    """
        A Django model mixin that adds timestamp fields to track the creation and last update time of an object.

        Attributes:
            created_at (DateTimeField): The timestamp representing the date and time when the object was created.
                                       Automatically set to the current date and time when the object is first saved.
            updated_at (DateTimeField): The timestamp representing the date and time when the object was last updated.
                                       Automatically updated to the current date and time whenever the object is saved again.
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True



