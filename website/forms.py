from django import forms
from .models import ContactMessage

class ContactForm(forms.ModelForm):
    website = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'honeypot', 'tabindex': '-1', 'autocomplete': 'off'}))

    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'company', 'project_type', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'required': True}),
            'email': forms.EmailInput(attrs={'required': True}),
            'company': forms.TextInput(),
            'project_type': forms.Select(attrs={'required': True}),
            'message': forms.Textarea(attrs={'rows': 5, 'required': True}),
        }

    def clean_website(self):
        value = self.cleaned_data.get('website', '').strip()
        if value:
            raise forms.ValidationError('Spam detected.')
        return value
