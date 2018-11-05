from django import forms
from report.models import UserReport




class ReportForm(forms.ModelForm):

    class Meta:
        model = UserReport
        fields = ('report_category', 'reason_for_report')
        widgets= {
 
                'reason_for_report': forms.Textarea(attrs={'cols':80, 'row': 20}),
            }
