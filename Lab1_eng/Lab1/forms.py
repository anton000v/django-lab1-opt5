from django import forms
from .models import Message
from django.contrib.auth.models import User

class UserMessageForm(forms.ModelForm):
    # phone_number = PhoneNumberField()
    # wishes = forms.CharField(widget=forms.Textarea)
    # recipient = forms.ChoiceField( widget=forms.Select(attrs={'readonly': True}))

    class Meta:
        model = Message
        exclude = ('pub_date',)
