from django import forms
from .models import employee
class EmployeeForm(forms.ModelForm):
    class Meta:
        model=employee
        fields='__all__'
    def __init__(self,*args,**kwargs):
        super(EmployeeForm,self).__init__(*args,**kwargs)
        self.fields['Position'].empty_label='select'
        self.fields['EmpCode'].required=False

