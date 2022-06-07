"Custom mixins for task_manager app."

from django.contrib.auth.mixins import AccessMixin
from django.contrib import messages
from django.urls import reverse_lazy
from django.db.models import ProtectedError
from django.http import HttpResponseRedirect
from task_manager.labels.constants import (
    ERROR_LABEL_IN_USE,
    LABEL_DELETED,
)
from task_manager.statuses.constants import (
    ERROR_STATUS_IN_USE,
    STATUS_DELETED,
)
from task_manager.users.constants import (
    ERROR_USER_IN_USE,
    USER_DELETED,
)

SUCCESS_URLS = {
    'User': reverse_lazy('users:list'),
    'Status': reverse_lazy('statuses:list'),
    'Label': reverse_lazy('labels:list'),
}
SUCCESS_MESSAGES = {
    'User': USER_DELETED,
    'Status': STATUS_DELETED,
    'Label': LABEL_DELETED,
}
ERROR_MESSAGES = {
    'User': ERROR_USER_IN_USE,
    'Status': ERROR_STATUS_IN_USE,
    'Label': ERROR_LABEL_IN_USE,
}


class FormValidMixin(AccessMixin):
    "Check if any other objects are linked to the given object."

    def form_valid(self, form):
        "Check if there are any tasks assigned to the given status."
        try:
            model_name = str(self.object.__class__.__name__)
            self.object.delete()
        except ProtectedError:
            messages.error(self.request, ERROR_MESSAGES[model_name])
        else:
            messages.success(self.request, SUCCESS_MESSAGES[model_name])
        return HttpResponseRedirect(SUCCESS_URLS[model_name])
