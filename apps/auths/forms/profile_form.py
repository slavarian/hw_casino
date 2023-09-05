from django import forms
from models.my_user import MyUser


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = ('email', 'password', 'nickname',)