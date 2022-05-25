import django_filters
from django_filters.filters import ChoiceFilter, BooleanFilter
from django.forms import CheckboxInput
from django.db.models import Value
from django.db.models.functions import Concat
from django.contrib.auth import get_user_model
from task_manager.labels.models import Label
from task_manager.statuses.models import Status
from .models import Task
from .constants import (
    EXECUTIVE_LABEL,
    LABEL_LABEL,
    OWN_TASKS_LABEL,
    STATUS_LABEL,
)

User = get_user_model()


class FilterTasks(django_filters.FilterSet):
    "Filter the tasks."
    all_statuses = Status.objects.values_list('id', 'name', named=True).all()
    status = ChoiceFilter(
        label=STATUS_LABEL,
        choices=all_statuses,
    )
    all_executives = User.objects.values_list(
        'id',
        Concat('first_name', Value(' '), 'last_name'),
        named=True,
    ).all()
    executive = ChoiceFilter(
        label=EXECUTIVE_LABEL,
        choices=all_executives,
    )
    all_labels = Label.objects.values_list('id', 'name', named=True).all()
    label = ChoiceFilter(
        label=LABEL_LABEL,
        choices=all_labels,
    )
    own_task = BooleanFilter(
        label=OWN_TASKS_LABEL,
        widget=CheckboxInput(),
        method='filter_own_tasks',
        field_name='own_tasks',
    )


    def filter_own_tasks(self, queryset, name, value):
        """Filter own tasks.

        Parameters:
            queryset: filtered query,
            name: filter name,
            value: filter value.

        Returns:
            queryset.
        """
        if value:
            queryset = queryset.filter(created_by=self.request.user)
        return queryset


    class Meta:
        model = Task
        fields = ['status', 'executive', 'label']
