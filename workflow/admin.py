from django.contrib import admin

from workflow.models import WorkFlow, WorkSpace, WorkFlowTrigger


class WorkSpaceAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_by')


admin.site.register(WorkFlow)
admin.site.register(WorkSpace, WorkSpaceAdmin)
admin.site.register(WorkFlowTrigger)
