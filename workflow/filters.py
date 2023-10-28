from datetime import datetime

from django_filters import FilterSet, filters

from workflow.models import WorkFlowTrigger


class WorkFlowTriggerFilter(FilterSet):

    workflow_trigger_id = filters.CharFilter()
    lower_date_range = filters.CharFilter(field_name='started_at', method='lower_date_range_filter')
    higher_date_range = filters.CharFilter(field_name='started_at', method='higher_date_range_filter')

    def lower_date_range_filter(self, queryset, name, value):
        datetime_value = datetime.strptime(value, "%Y-%m-%d %H:%M:%S")
        return queryset.filter(started_at__gte=datetime_value)

    def higher_date_range_filter(self, queryset, name, value):
        datetime_value = datetime.strptime(value, "%Y-%m-%d %H:%M:%S")
        return queryset.filter(started_at__lte=datetime_value)

    class Meta:
        model = WorkFlowTrigger
        fields = (
           'workflow_trigger_id', 'started_at'
        )
