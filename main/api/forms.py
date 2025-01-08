from django import forms
from .models import UserUploadPictureInServer

class UserUploadPictureForm(forms.ModelForm):
    class Meta:
        model = UserUploadPictureInServer
        fields = ['user', 'upload_photo']