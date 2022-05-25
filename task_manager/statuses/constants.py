"Constants for Statuses application."

from django.utils.translation import gettext_lazy

# Buttons
BUTTON_NAME_TITLE = 'title'
BUTTON_TEXT = 'button_text'
CREATE_BUTTON = gettext_lazy('Create')
CHANGE_BUTTON = gettext_lazy('Change')
DELETE_BUTTON = gettext_lazy('Delete')

# Fixtures
STATUSES_FIXTURE = 'statuses.json'
TASKS_FIXTURE = 'tasks.json'
USERS_FIXTURE = 'users.json'

# Forms
NAME = 'name'

# Messages
STATUS_CREATED = gettext_lazy('Status successfully created')
STATUS_CHANGED = gettext_lazy('Status successfully changed')
STATUS_DELETED = gettext_lazy('Status successfully deleted')
ERROR_STATUS_IN_USE = gettext_lazy('Cannot delete a status in use')

# Models
STATUS_NAME = gettext_lazy('Name')
STATUS_CREATED_AT = gettext_lazy('Created at')
VERBOSE_NAME = gettext_lazy('Status')
VERBOSE_NAME_PL = gettext_lazy('Statuses')

# Templates
STATUS_LIST_TEMPLATE = 'statuses.html'
FORM_TEMPLATE = 'form.html'
DELETE_TEMPLATE = 'delete.html'

# Titles
STATUS_LIST_TITLE = gettext_lazy('Statuses')
CREATE_STATUS_TITLE = gettext_lazy('Create a status')
CHANGE_STATUS_TITLE = gettext_lazy('Change a status')
DELETE_STATUS_TITLE = gettext_lazy('Delete a status')
