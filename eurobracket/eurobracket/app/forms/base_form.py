from django import forms


class BaseForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super(BaseForm, self).__init__(*args, **kwargs)

        for key in self.fields:
            field = self.fields[key]
            if field.required:
                field.error_messages = {'required': '{fieldname} is required'.format(
                    fieldname=field.label)}