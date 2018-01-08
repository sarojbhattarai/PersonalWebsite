from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from crispy_forms.layout import Field, Layout, Fieldset, ButtonHolder, Submit, HTML
from crispy_forms.bootstrap import *


class ContactForm(forms.Form):
    name = forms.CharField(
        label = 'Your Name',
        max_length = 50
        )
    email = forms.EmailField(
        label = 'Your Favourite Email')
    subject = forms.CharField()
    message = forms.CharField(
        label = 'Your Message',
        widget = forms.Textarea
        )


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
                    "Keep in touch",
                    'name',
                    'email',
                    'subject',
                    'message'
                ),
            ButtonHolder(
                Submit('submit', 'Send', css_class = 'btn btn-primary'))

            )

