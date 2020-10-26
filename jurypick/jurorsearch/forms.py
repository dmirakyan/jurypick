from django import forms
from django.db.models.fields import BLANK_CHOICE_DASH
from localflavor.us.forms import USZipCodeField
from jurorsearch.models import Query, Profile
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column


STATE_CHOICES = (('AL', 'Alabama'), ('AK', 'Alaska'), ('AS', 'American Samoa'), ('AZ', 'Arizona'), ('AR', 'Arkansas'), ('AA', 'Armed Forces Americas'), ('AE', 'Armed Forces Europe'), ('AP', 'Armed Forces Pacific'), ('CA', 'California'), ('CO', 'Colorado'), ('CT', 'Connecticut'), ('DE', 'Delaware'), ('DC', 'District of Columbia'), ('FL', 'Florida'), ('GA', 'Georgia'), ('GU', 'Guam'), ('HI', 'Hawaii'), ('ID', 'Idaho'), ('IL', 'Illinois'), ('IN', 'Indiana'), ('IA', 'Iowa'), ('KS', 'Kansas'), ('KY', 'Kentucky'), ('LA', 'Louisiana'), ('ME', 'Maine'), ('MD', 'Maryland'), ('MA', 'Massachusetts'), ('MI', 'Michigan'), ('MN', 'Minnesota'), ('MS', 'Mississippi'), ('MO', 'Missouri'), ('MT', 'Montana'), ('NE', 'Nebraska'), ('NV', 'Nevada'), ('NH', 'New Hampshire'), ('NJ', 'New Jersey'), ('NM', 'New Mexico'), ('NY', 'New York'), ('NC', 'North Carolina'), ('ND', 'North Dakota'), ('MP', 'Northern Mariana Islands'), ('OH', 'Ohio'), ('OK', 'Oklahoma'), ('OR', 'Oregon'), ('PA', 'Pennsylvania'), ('PR', 'Puerto Rico'), ('RI', 'Rhode Island'), ('SC', 'South Carolina'), ('SD', 'South Dakota'), ('TN', 'Tennessee'), ('TX', 'Texas'), ('UT', 'Utah'), ('VT', 'Vermont'), ('VI', 'Virgin Islands'), ('VA', 'Virginia'), ('WA', 'Washington'), ('WV', 'West Virginia'), ('WI', 'Wisconsin'), ('WY', 'Wyoming'))


class QueryForm(forms.ModelForm):
    first_name = forms.CharField(
        max_length=128, 
        widget=forms.TextInput(attrs={'placeholder': 'John'}),
        required=False)
    middle_name = forms.CharField(
        max_length=128, 
        required=False)
    last_name = forms.CharField(       
        max_length=128, 
        widget=forms.TextInput(attrs={'placeholder': 'Smith'}),
        required=False)
    address = forms.CharField(
        max_length=128,
        widget=forms.TextInput(attrs={'placeholder': '1234 Main St'}),
        required=False)
    city = forms.CharField(
        max_length=128, 
        required=False)
    state = forms.ChoiceField(
        required=False, 
        choices=(('', 'state'),)+STATE_CHOICES)
    zip_code = USZipCodeField(
        required=False,
    )
    class Meta:
        model = Query
        exclude = ('search_id',)
    
   