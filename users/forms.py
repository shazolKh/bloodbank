from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class RegForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']


class UserProfileForm(forms.Form):
    class Meta:
        model = User
        # fields = ['age', 'blood_group', 'weight', 'gender', 'mobile', 'mobile2', 'address', 'disease']
        exclude = ('user', )