from django import forms
from django.db.models.fields import BLANK_CHOICE_DASH
from localflavor.us.forms import USZipCodeField
from jurorsearch.models import Query, Human
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column


STATE_CHOICES = (('AL', 'Alabama'), ('AK', 'Alaska'), ('AS', 'American Samoa'), ('AZ', 'Arizona'), ('AR', 'Arkansas'), ('AA', 'Armed Forces Americas'), ('AE', 'Armed Forces Europe'), ('AP', 'Armed Forces Pacific'), ('CA', 'California'), ('CO', 'Colorado'), ('CT', 'Connecticut'), ('DE', 'Delaware'), ('DC', 'District of Columbia'), ('FL', 'Florida'), ('GA', 'Georgia'), ('GU', 'Guam'), ('HI', 'Hawaii'), ('ID', 'Idaho'), ('IL', 'Illinois'), ('IN', 'Indiana'), ('IA', 'Iowa'), ('KS', 'Kansas'), ('KY', 'Kentucky'), ('LA', 'Louisiana'), ('ME', 'Maine'), ('MD', 'Maryland'), ('MA', 'Massachusetts'), ('MI', 'Michigan'), ('MN', 'Minnesota'), ('MS', 'Mississippi'), ('MO', 'Missouri'), ('MT', 'Montana'), ('NE', 'Nebraska'), ('NV', 'Nevada'), ('NH', 'New Hampshire'), ('NJ', 'New Jersey'), ('NM', 'New Mexico'), ('NY', 'New York'), ('NC', 'North Carolina'), ('ND', 'North Dakota'), ('MP', 'Northern Mariana Islands'), ('OH', 'Ohio'), ('OK', 'Oklahoma'), ('OR', 'Oregon'), ('PA', 'Pennsylvania'), ('PR', 'Puerto Rico'), ('RI', 'Rhode Island'), ('SC', 'South Carolina'), ('SD', 'South Dakota'), ('TN', 'Tennessee'), ('TX', 'Texas'), ('UT', 'Utah'), ('VT', 'Vermont'), ('VI', 'Virgin Islands'), ('VA', 'Virginia'), ('WA', 'Washington'), ('WV', 'West Virginia'), ('WI', 'Wisconsin'), ('WY', 'Wyoming'))


class QueryForm(forms.ModelForm):
    first_name = forms.CharField(
        max_length=128, 
        widget=forms.TextInput(),
        required=False)
    middle_name = forms.CharField(
        max_length=128, 
        required=False)
    last_name = forms.CharField(       
        max_length=128, 
        widget=forms.TextInput(),
        required=False)
    address = forms.CharField(
        max_length=128,
        label='Address or County',
        widget=forms.TextInput(),
        required=False)
    city = forms.CharField(
        max_length=128, 
        required=False)
    state = forms.ChoiceField(
        required=False, 
        choices=(('', 'state'),)+STATE_CHOICES)
    zip_code = forms.CharField(
        max_length=128,
        label='Zip',
        required=False,)
    email = forms.CharField(
        max_length=128, 
        required=False)
    phone = forms.CharField(
        max_length=128, 
        required=False)
    birth_date = forms.CharField(
        widget=forms.TextInput(),
        required=False)

    class Meta:
        model = Query
        exclude = ('search_id','author','created_at')
    
class ContactForm(forms.Form):
    name = forms.CharField(
            required=True,
            # label='name'
            # widget=forms.TextInput(attrs={'placeholder': 'required'})
            )
    email = forms.EmailField(
            required=True,
            # widget=forms.TextInput(attrs={'placeholder': 'required'})
    )
    phone = forms.CharField(required=False)
    message = forms.CharField(widget=forms.Textarea(attrs={'rows': 5}), required=False)