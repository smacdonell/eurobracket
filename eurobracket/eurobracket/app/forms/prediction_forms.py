from django import forms
from django.core.exceptions import ValidationError

from eurobracket.app.forms.base_form import BaseForm
import json


class PredictionForm(BaseForm):
    error_messages = {
        'not_valid': 'JSON not valid',
        'missing_predictions': 'You must fill out all predictions'
    }

    rounds = {
        'ROUND_OF_SIXTEEN': 8,
        'QUARTER_FINALS': 4,
        'SEMI_FINALS': 2,
        'FINALS': 1
    }

    pred_data = forms.CharField(required=True)

    def clean_pred_data(self):
        pred_data = None
        try:
            pred_data = json.loads(self.cleaned_data.get('pred_data'))
            if len(pred_data['games']) < self.rounds[pred_data['round']]:
                raise ValidationError(
                    self.error_messages['missing_predictions'],
                    code='missing_predictions'
                )
        except ValueError:
            raise ValidationError(
                self.error_messages['not_valid'],
                code='not_valid'
            )

        return pred_data

    def clean(self):
        cd = super().clean()
