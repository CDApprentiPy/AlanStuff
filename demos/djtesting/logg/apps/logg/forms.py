from django import forms

class LogForm(forms.Form):
    "Log In Form"
    email = forms.EmailField(min_length=10)
    password = forms.CharField(min_length=10, max_length=50, widget=forms.PasswordInput)

class RegForm(forms.Form):
    "Fo' registerin'"
    name = forms.CharField(min_length=2, max_length=50)
    email = forms.EmailField(min_length=10)
    password = forms.CharField(min_length=10, max_length=50, widget=forms.PasswordInput)
    password_confirm = forms.CharField(min_length=10, max_length=50, widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super(RegForm, self).clean()
        pw1 = cleaned_data.get("password")
        pw2 = cleaned_data.get("password_confirm")

        if pw2 != pw1:
            self.add_error('password', "Yo, this has gotta be the same as that!")
