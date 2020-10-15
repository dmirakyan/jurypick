from django import forms
from jurorsearch.models import Query, Profile

class QueryForm(forms.ModelForm):
    first_name = forms.CharField(max_length=128, help_text='First name')
    # middle_name = forms.CharField(max_length=128, help_text='Middle name')
    last_name = forms.CharField(max_length=128, help_text='Last name')
    # address = forms.CharField(max_length=128, help_text='address')
    # city = forms.CharField(max_length=128, help_text='city')
    # state = forms.CharField(max_length=128, help_text='state')
    zip_code = forms.IntegerField(help_text='zip code',widget=forms.NumberInput)
    # search_id = forms.AutoField(widget=forms.HiddenInput(),required=False)


    class Meta: 
        model = Query
        # exclude = ('search_id',)
        fields = ('first_name','last_name','zip_code')
