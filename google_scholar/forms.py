from django import forms

from google_scholar.models import Author


class AuthorForm(forms.ModelForm):
    class Meta:
        model=Author
        fields='__all__'

    def clean_first_name(self):
        return self.cleaned_data['first_name'].strip()

    def clean_last_name(self):
        return self.cleaned_data['last_name'].strip()

    def clean_birth_year(self):
        return self.cleaned_data['birth_year'].strip()

    def clean_affiliation(self):
        return self.cleaned_data['affiliation'].strip()

    def clean_country(self):
        return self.cleaned_data['country'].strip()
