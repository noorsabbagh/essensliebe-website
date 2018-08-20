from django import forms

LEVELS = (
        ('Mandatory', 'Mandatory'),
        ('Very Important', 'Very Important'),
        ('Somewhat Important', 'Somewhat Important'),
        ('Not Important', 'Not Importan'),
        )

class UserResponseForm(forms.Form):
    question_id = forms.IntegerField()
    answer_id = forms.IntegerField()
    importance_level = forms.ChoiceField(choices=LEVELS)
    partner_answer_id = forms.IntegerField()
    partner_importance_level = forms.ChoiceField(choices=LEVELS)