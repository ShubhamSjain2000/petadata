from django.contrib import admin

from workflow.models import WorkFlow, WorkSpace, WorkFlowTrigger


class WorkSpaceAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_by')

class WorkflowAdmin(admin.ModelAdmin):
    readonly_fields=('created_at', 'updated_at')

admin.site.register(WorkFlow, WorkflowAdmin)
admin.site.register(WorkSpace, WorkSpaceAdmin)
admin.site.register(WorkFlowTrigger)
