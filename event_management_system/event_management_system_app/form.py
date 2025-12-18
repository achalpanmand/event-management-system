from django import forms
from .models import Registration, Feedback

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ['event']

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['comments', 'rating']
