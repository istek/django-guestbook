from django import forms
from .models import Guestbook

class MessageForm(forms.ModelForm):
    class Meta:
        model=Guestbook
        fields=('name','email','avatar','weburl','content')