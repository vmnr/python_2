from socket import fromshare
from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    date_of_birth = forms.DateTimeField(
                    label='Date Of Birth:',
                    input_formats=['%d/%m/%Y'],
                    required=False)
                        
    class Meta:
        model = Employee
        # fields = '__all__'
        fields = fields = ['first_name', 'last_name', 'email_id', 'phone_number', 'date_of_birth']