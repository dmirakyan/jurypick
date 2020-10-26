
from django.http import HttpResponse, JsonResponse
import requests

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
    return json_response

def parse_person(json_response):
    person_details = json_response['data']
    school_count = len(person_details['education'])
    facebook_id = person_details['facebook_id']
    fb_key = "643286449673767|3BW8OSQfjmlb6EP1fy055lVZ9pE"

    if facebook_id:
        fb_profile = f"https://graph.facebook.com/v8.0/{facebook_id}/picture?redirect=true&access_token={fb_key}"
    
    person_clean = {
        #"raw_record": json_response,
        "record_id": person_details['id'],
        
        # Demographics
        "age": person_details['birth_year'],
        "person_full_name": person_details['full_name'].title(),
        
        # Social profiles
        "facebook_url": person_details['facebook_url'],
        "facebook_id": person_details['facebook_id'],
        # "facebook_image":'//graph.facebook.com/'+facebook_id+'/picture',
        "linkedin_url": person_details['linkedin_url'],
        "twitter_url": person_details['twitter_url'],
        
        # Work details
        "job_title": person_details['job_title'],
        "industry": person_details['industry'],
        "job_company_name": person_details['job_company_name'],
        "job_company_url": person_details['job_company_website'],
    }
    
    
    for n in range(school_count):
        if n == 0:
            person_clean["school_name_1"] = person_details['education'][0]['school']['name']
            person_clean["school_url_1"] = person_details['education'][0]['school']['website']
            person_clean["school_gpa_1"] = person_details['education'][0]['gpa']
            person_clean["school_start1"] = person_details['education'][0]['start_date']
            person_clean["school_stop1"] = person_details['education'][0]['end_date']  
        if n == 1:
            person_clean["school_name_2"] = person_details['education'][1]['school']['name']
            person_clean["school_url_2"] = person_details['education'][1]['school']['website']
            person_clean["school_gpa_2"] = person_details['education'][1]['gpa']
            person_clean["school_start2"] = person_details['education'][1]['start_date']
            person_clean["school_stop2"] = person_details['education'][1]['end_date'] 
        if n == 2:
            person_clean["school_name_3"] = person_details['education'][2]['school']['name']
            person_clean["school_url_3"] = person_details['education'][2]['school']['website']
            person_clean["school_gpa_3"] = person_details['education'][2]['gpa']
            person_clean["school_start3"] = person_details['education'][2]['start_date']
            person_clean["school_stop3"] = person_details['education'][2]['end_date'] 
    
    return person_clean