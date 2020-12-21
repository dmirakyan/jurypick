from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.utils import timezone

# import requests


from jurorsearch.forms import QueryForm
from jurorsearch.enrich import call_api, parse_person, check_response_status
from jurorsearch.models import Query, Human

import json


# Create your views here.

# def index(request):
#     # return HttpResponse('Test page')
#     return render(request,'jurorsearch/index.html')
@login_required
def history(request):
    if request.user.is_authenticated:
        user=request.user
        searches=Human.objects.filter(author=user.id).filter(response_status=200).order_by('-created_at')
        # return render(request,"display.html",{'obj_list':search_list})
        return render(request,'jurorsearch/history.html',{'searches':searches})
        return render(request,reverse('auth_login'),{'searches':searches})

    else:
        # return render(request,'accounts:login')
        return redirect(reverse('auth_login'))


def index(request):
    if request.user.is_authenticated:
        # return HttpResponse('Logged in')
        form = QueryForm
        if request.method == 'POST':
            form = QueryForm(request.POST)
            if form.is_valid():
                query = form.save(commit=False)
                query.author = request.user
                query.created_at = timezone.now()
                query.save()

                # Make the request?
                json_response = call_api(form)
                person_clean = parse_person(json_response)
                json_raw = json.dumps(json_response)
                json_parsed = json.dumps(person_clean)
                response_status = check_response_status(json_response)
                human = Human.objects.create(search_id = query, author=request.user, result=json_raw, result_clean=json_parsed, result_clean_json=person_clean, hidden=False,response_status=response_status,created_at=timezone.now())
                human.save()
                # return JsonResponse(person_clean)  
                return render(request,'jurorsearch/index.html',{'form':form, 'person':person_clean, 'json_raw':json_raw,'json_parsed':json_parsed})
            else:
                print(form.errors)
        return render(request,'jurorsearch/index.html',{'form':form})
    else:
        # return render(request,'accounts:login')
        return redirect(reverse('auth_login'))


