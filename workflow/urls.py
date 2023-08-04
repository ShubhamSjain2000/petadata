from django.urls import path, include
from rest_framework.routers import DefaultRouter

from workflow.views import WorkSpaceViewSet, WorkFlowViewSet, WorkFlowTriggerViewSet


router = DefaultRouter()
router.register(r'workspace', WorkSpaceViewSet, basename="workspace")
# router.register('abcd/workflow', WorkFlowViewSet, basename="workflow")
router.register(r'(?P<workspace_id>[-\w]+)/workflow',WorkFlowViewSet)
router.register(r'(?P<workflow_id>[-\w]+)/workflowtrigger', WorkFlowTriggerViewSet,
                basename="workflowtrigger")


urlpatterns = [
    path('', include(router.urls)),
]
