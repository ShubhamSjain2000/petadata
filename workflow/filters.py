from rest_framework.filters import BaseFilterBackend
from workflow.models import WorkSpace


class WorkSpaceFilterBackend(BaseFilterBackend):

    class Meta:
        model = WorkSpace
        fields = {
            'name': ['startswith']
        }