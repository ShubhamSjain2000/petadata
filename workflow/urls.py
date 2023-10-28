from django.urls import path, include
from rest_framework.routers import DefaultRouter

from workflow.viewsets import WorkSpaceViewSet, WorkFlowViewSet, WorkFlowTriggerViewSet
from workflow.views import WorkSpaceListView, WorkSpaceCreateView


router = DefaultRouter()
router.register(r'workspace', WorkSpaceViewSet, basename="workspace")
router.register(r'(?P<workspace_id>[-\w]+)/workflow',WorkFlowViewSet)
router.register(r'(?P<workflow_id>[-\w]+)/workflowtrigger', WorkFlowTriggerViewSet, basename="workflowtrigger")


urlpatterns = [
    path('', include(router.urls)),
    path('ui/workspace/', WorkSpaceListView.as_view()),
    path('ui/workspace/create', WorkSpaceCreateView.as_view())
]
