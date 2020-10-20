from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from jurorsearch.forms import QueryForm
import requests

# Create your views here.

# def index(request):
#     # return HttpResponse('Test page')
#     return render(request,'jurorsearch/index.html')

def call_api(form):
    key = 'f2941a3b96cf342515290aed8576caffa54ca7cc00c3acf4e148527437a2b0a0'
    rq_url = "https://api.peopledatalabs.com/v5/person/enrich"

    first_name = form.cleaned_data['first_name']
    middle_name = form.cleaned_data['middle_name']
    last_name = form.cleaned_data['last_name']
    address = form.cleaned_data['address']
    city = form.cleaned_data['city']
    state = form.cleaned_data['state']
    postal_code = form.cleaned_data['zip_code']


    test_params = {
        "api_key": key,
        "country":["United States"],
        "first_name": [first_name],
        "middle_name": [middle_name],
        "last_name": [last_name],
        "strees_address": [address],
        "locality": [city],
        "region":[state],
        "postal_code":[postal_code]
    }

    json_response = requests.get(rq_url,  params=test_params).json()
    # return test_params
    return json_response



def index(request):
    form = QueryForm
    if request.method == 'POST':
        form = QueryForm(request.POST)
        if form.is_valid():
            # form.save(commit=True)
            # Make the request?
            result = call_api(form)
            return JsonResponse(result)  
        else:
            print(form.errors)
    return render(request,'jurorsearch/index.html',{'form':form})

