from django import forms
from main.models import *


class MessageForm(forms.ModelForm):
    class Meta:
        model = MessageModel
        fields = ['user_name', 'email', 'subject', 'message']