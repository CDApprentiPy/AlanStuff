from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

class RegForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("first_name","username", "password1", "password2")
        labels = {
            'first_name': _('name')
        }

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        for fieldname in ["first_name",'username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None