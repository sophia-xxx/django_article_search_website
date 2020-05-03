from django import forms

from google_scholar.models import Author, Journal, Article


class AuthorForm(forms.ModelForm):
    class Meta:
        model=Author
        fields='__all__'

    def clean_first_name(self):
        return self.cleaned_data['first_name'].strip()

    def clean_last_name(self):
        return self.cleaned_data['last_name'].strip()


    def clean_affiliation(self):
        return self.cleaned_data['affiliation'].strip()

    def clean_country(self):
        return self.cleaned_data['country'].strip()


class JournalForm(forms.ModelForm):
    class Meta:
        model=Journal
        fields='__all__'

    def clean_journal_name(self):
        return self.cleaned_data['journal_name'].strip()
    def clean_image_url(self):
        return self.cleaned_data['image_url'].strip()
    def clean_introduction(self):
        return self.cleaned_data['introduction'].strip()

class ArticleForm(forms.ModelForm):
    class Meta:
        model=Article
        fields='__all__'

    def clean_title(self):
        return self.cleaned_data['title'].strip()

    def clean_pub_url(self):
        return self.cleaned_data['pub_url'].strip()
