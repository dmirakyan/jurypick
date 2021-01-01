from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.utils import timezone
from .serializers import ResultSerializer

# import requests


from jurorsearch.forms import QueryForm
from jurorsearch.enrich import call_api, parse_person, check_response_status
from jurorsearch.models import Query, Human, UserDetail

from rest_framework.decorators import api_view
from rest_framework.response import Response


import json


# Create your views here.

# def index(request):
#     # return HttpResponse('Test page')
#     return render(request,'jurorsearch/index.html')
@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'hide': '/hide-modal/<int:pk>/',
        'favorite': '/favorite-modal/<int:pk>/',
        'user': '/user/<int:pk>',
        'users': '/users/',
        }
    return Response(api_urls)

@api_view(['GET'])
def humanList(request):
    humans = Human.objects.all()
    serializer = ResultSerializer(humans, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def humanDetails(request,pk):
    humans = Human.objects.get(search_id=pk)
    serializer = ResultSerializer(humans, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def humanUpdate(request,pk):
    human = Human.objects.get(search_id=pk)
    serializer = ResultSerializer(instance=human, data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def humanHide(request,pk):
    human = Human.objects.get(search_id=pk)
    update = human
    update.hidden = True
    serializer = ResultSerializer(instance=human, data = update)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)



@login_required
def hideHuman(self, pk):
        search_id = pk
        try:
            human = Human.objects.get(search_id=search_id)
        except human.DoesNotExist:
            return HttpResponse(-1)
        human.hidden = True
        human.save()
        return HttpResponse('it worked?')
        
@login_required
def unhideAllHumans(request):
        if request.user.is_authenticated:
            user=request.user
            searches=Human.objects.filter(author=user.id).filter(response_status=200)
            for human in searches:
                human.hidden = False
                human.save()
            return redirect('/jurorsearch/history.html')
        else:
            return redirect(reverse('auth_login'))
        return HttpResponse('it worked?')

@login_required
def starHuman(self, pk):
        search_id = pk

        try:
            human = Human.objects.get(search_id=search_id)
        except human.DoesNotExist:
            return HttpResponse(-1)

        if human.starred == True:
            human.starred = False
        else:
            human.starred = True

        human.save()
        return HttpResponse('it worked?')



@login_required
def history(request):
    if request.user.is_authenticated:
        user=request.user
        searches=Human.objects.filter(author=user.id).filter(response_status=200,hidden=False).order_by('-created_at')
        return render(request,'jurorsearch/history.html',{'searches':searches})

    else:
        # return render(request,'accounts:login')
        return redirect(reverse('auth_login'))

@login_required
def powertools(request):
    if request.user.is_authenticated:
        user=request.user
        searches=Human.objects.filter(author=user.id).filter(response_status=200,hidden=False).order_by('-created_at')
        return render(request,'jurorsearch/powertools.html',{'searches':searches})
    else:
        return redirect(reverse('auth_login'))


def index(request):
    if request.user.is_authenticated:
        # return HttpResponse('Logged in')
        form = QueryForm
        userdetail = UserDetail.objects.get(user=request.user)
        credits = userdetail.credits
        if request.method == 'POST':
            form = QueryForm(request.POST)
            if form.is_valid():
                if credits > 0:
                    userdetail.credits -= 1
                    userdetail.save()
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
                    person = {
                        "status" : 400,
                        "error": {
                            "message": 'no searches left',
                        },
                    }
                    return render(request,'jurorsearch/index.html',{'form':form, 'person':person})
            else:
                print(form.errors)
        return render(request,'jurorsearch/index.html',{'form':form})
    else:
        # return render(request,'accounts:login')
        return redirect(reverse('auth_login'))


