from django import forms

class BadgeUploadForm(forms.Form):
    badge = forms.ImageField()
