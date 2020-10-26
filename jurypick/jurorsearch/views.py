from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
# import requests

from jurorsearch.forms import QueryForm
from jurorsearch.enrich import call_api, parse_person
import json


# Create your views here.

# def index(request):
#     # return HttpResponse('Test page')
#     return render(request,'jurorsearch/index.html')



def index(request):
    form = QueryForm
    if request.method == 'POST':
        form = QueryForm(request.POST)
        if form.is_valid():
            # form.save(commit=True)
            # Make the request?
            json_response = call_api(form)
            person_clean = parse_person(json_response)
            json_raw = json.dumps(json_response)
            json_parsed = json.dumps(person_clean)
            # return JsonResponse(person_clean)  
            return render(request,'jurorsearch/index.html',{'form':form, 'person':person_clean, 'json_raw':json_raw,'json_parsed':json_parsed})
        else:
            print(form.errors)
    return render(request,'jurorsearch/index.html',{'form':form})

