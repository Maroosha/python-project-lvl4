"Constants for Labels application."

from django.utils.translation import gettext_lazy

# Buttons
BUTTON_NAME_TITLE = 'title'
BUTTON_TEXT = 'button_text'
CREATE_BUTTON = gettext_lazy('Create')
CHANGE_BUTTON = gettext_lazy('Change')
DELETE_BUTTON = gettext_lazy('Delete')

# Fixtures
LABELS_FIXTURE = 'labels.json'
STATUSES_FIXTURE = 'statuses.json'
TASKS_FIXTURE = 'tasks.json'
TASKLABELRELATION_FIXTURE = 'tasklabelrelation.json'
USERS_FIXTURE = 'users.json'

# Forms
NAME = 'name'

# Messages
LABEL_CREATED = gettext_lazy('Label successfully created')
LABEL_CHANGED = gettext_lazy('Label successfully changed')
LABEL_DELETED = gettext_lazy('Label successfully deleted')
ERROR_LABEL_IN_USE = gettext_lazy('Cannot delete a label in use')

# Models
LABEL_CREATED_AT = gettext_lazy('Created at')
LABEL_NAME = gettext_lazy('Name')
VERBOSE_NAME = gettext_lazy('Label')
VERBOSE_NAME_PL = gettext_lazy('Labels')

# Templates
LABEL_LIST_TEMPLATE = 'labels.html'
FORM_TEMPLATE = 'form.html'
DELETE_TEMPLATE = 'delete.html'

# Titles
LABEL_LIST_TITLE = gettext_lazy('Labels')
CREATE_LABEL_TITLE = gettext_lazy('Create a label')
CHANGE_LABEL_TITLE = gettext_lazy('Change a label')
DELETE_LABEL_TITLE = gettext_lazy('Delete a label')
