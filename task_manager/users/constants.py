"Constants for Users application."

from django.utils.translation import gettext_lazy

# Buttons
BUTTON_NAME_TITLE = 'title'
BUTTON_TEXT = 'button_text'
REGISTER_BUTTON = gettext_lazy('Register')
CHANGE_BUTTON = gettext_lazy('Change')
DELETE_BUTTON = gettext_lazy('Delete')

# Fixtures
STATUSES_FIXTURE = 'statuses.json'
TASKS_FIXTURE = 'tasks.json'
USERS_FIXTURE = 'users.json'

# Forms
FIRST_NAME = 'first_name'
LAST_NAME = 'last_name'
PASSWORD1 = 'password1'
PASSWORD2 = 'password2'
USERNAME = 'username'

# Messages
CANT_CHANGE_ANOTHER_USER = gettext_lazy('You do not have a permission to change \
another user')
LOGIN_REQUIRED = gettext_lazy('You are not authorized. Please, log in.')
USER_CREATED = gettext_lazy('User successfully created')
USER_CHANGED = gettext_lazy('User successfully changed')
USER_DELETED = gettext_lazy('User successfully deleted')
ERROR_USER_IN_USE = gettext_lazy('Cannot delete a user in use')

# Models
VERBOSE_NAME = gettext_lazy('User')
VERBOSE_NAME_PL = gettext_lazy('Users')

# Templates
USER_LIST_TEMPLATE = 'users.html'
FORM_TEMPLATE = 'form.html'
DELETE_TEMPLATE = 'delete.html'

# Titles
USER_LIST_TITLE = gettext_lazy('Users')
CREATE_USER_TITLE = gettext_lazy('Create a user')
CHANGE_USER_TITLE = gettext_lazy('Change a user')
DELETE_USER_TITLE = gettext_lazy('Delete a user')
