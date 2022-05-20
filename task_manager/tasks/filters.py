from random import choices
import django_filters
from django_filters.filters import ChoiceFilter, BooleanFilter
from django.forms import CheckboxInput
from django.db.models import Value
from django.db.models.functions import Concat
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy
from .models import Task
from task_manager.labels.models import Label
from task_manager.statuses.models import Status

User = get_user_model()


class FilterTasks(django_filters.FilterSet):
    "Filter the tasks."
    all_statuses = Status.objects.values_list('id', 'name', named=True).all()
    status = ChoiceFilter(
        label=gettext_lazy('Status'),
        choices=all_statuses,
    )
    all_executives = User.objects.values_list(
        'id',
        Concat('first_name', Value(' '), 'last_name'),
        named=True,
    ).all()
    executive = ChoiceFilter(
        label=gettext_lazy('Executive'),
        choices=all_executives,
    )
    all_labels = Label.objects.values_list('id', 'name', named=True).all()
    label = ChoiceFilter(
        label=gettext_lazy('Label'),
        choices=all_labels,
    )
    own_tasks = BooleanFilter(
        label=gettext_lazy('my tasks only'),
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
        fields = ['status', 'executive', 'labels']
