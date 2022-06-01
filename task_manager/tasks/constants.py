"Constants for Tasks application."

from django.utils.translation import gettext_lazy

# Buttons
BUTTON_NAME_TITLE = 'title'
BUTTON_TEXT = 'button_text'
CREATE_BUTTON = gettext_lazy('Create')
CHANGE_BUTTON = gettext_lazy('Change')
DELETE_BUTTON = gettext_lazy('Yes, delete')
SHOW_BUTTON = gettext_lazy('Show')

# Filters
EXECUTIVE_LABEL = gettext_lazy('Executive')
LABEL_LABEL = gettext_lazy('Label')
OWN_TASKS_LABEL = gettext_lazy('my tasks only')
STATUS_LABEL = gettext_lazy('Status')

# Fixtures
LABELS_FIXTURE = 'labels.json'
STATUSES_FIXTURE = 'statuses.json'
TASKS_FIXTURE = 'tasks.json'
TASKLABELRELATION_FIXTURE = 'tasklabelrelation.json'
USERS_FIXTURE = 'users.json'

# Forms
NAME = 'name'
DESCRIPTION = 'description'
STATUS = 'status'
CREATED_BY = 'created_by'
EXECUTIVE = 'executor'
LABEL = 'labels'
TASK_NAME = gettext_lazy('Name')
TASK_DESCRIPTION = gettext_lazy('Description')
TASK_STATUS = gettext_lazy('Status')
TASK_EXECUTIVE = gettext_lazy('Executive')
TASK_LABEL = gettext_lazy('Labels')

# Messages
TASK_CREATED = gettext_lazy('Task successfully created')
TASK_CHANGED = gettext_lazy('Task successfully changed')
TASK_DELETED = gettext_lazy('Task successfully deleted')
ERROR_DELETE_TASK_BY_NONCREATOR = gettext_lazy('The task can only be deleted \
by its creator')

# Models
TASK_CREATED_BY = 'Created_by'
TASK_CREATED_AT = gettext_lazy('Created at')

# Templates
TASK_LIST_TEMPLATE = 'tasks.html'
TASK_VIEW_TEMPLATE = 'task_view.html'
FORM_TEMPLATE = 'form.html'
DELETE_TEMPLATE = 'delete.html'
VERBOSE_NAME = gettext_lazy('Task')
VERBOSE_NAME_PL = gettext_lazy('Tasks')

# Titles
TASK_LIST_TITLE = gettext_lazy('Tasks')
TASK_VIEW_TITLE = gettext_lazy('Task view')
CREATE_TASK_TITLE = gettext_lazy('Create a task')
CHANGE_TASK_TITLE = gettext_lazy('Change a task')
DELETE_TASK_TITLE = gettext_lazy('Delete a task')
