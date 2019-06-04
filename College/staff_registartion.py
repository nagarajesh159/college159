from django import forms
from .models import StaffRegistration
from django.contrib.auth.models import User


#class StaffRegistrationForm(forms.ModelForm):
#    class Meta:
#        model = StaffRegistration
#        exclude = ('user', 'email')


#class StaffUserForm(forms.Form):
#    username = forms.CharField(max_length=100)
#    password = forms.CharField(widget=forms.PasswordInput)
#    email = forms.EmailField()

#    class Meta:
#        model = User
#        fields = ('username', 'password', 'email')


class StaffUserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username', 'password','email')



class StaffRegistrationForm(forms.ModelForm):
    class Meta:
        model = StaffRegistration
        fields = ('name', 'age', 'gender', 'department', 'profile_pic')