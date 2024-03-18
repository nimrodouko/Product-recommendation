from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    gender = forms.ChoiceField(choices=CustomUser.GENDER_CHOICES, widget=forms.RadioSelect)
    location = forms.ChoiceField(choices=CustomUser.LOCATION, widget=forms.RadioSelect)
    
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('age','gender','budget','location',)

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields