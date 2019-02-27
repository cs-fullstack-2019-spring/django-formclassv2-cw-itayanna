
# importing forms info

from django import forms



#name, date of birth, position applying to, and salary



class jobApp(forms.Form):
    name = forms.CharField()
    dateOfBirth = forms.DateField()
    positionApplyingTo = forms.CharField()
    salary = forms.DecimalField()
