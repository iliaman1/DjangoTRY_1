from django import forms
from users.models import CustomUser


class ProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['ava', 'username', 'slug']