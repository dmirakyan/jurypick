
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
    phone = form.cleaned_data['phone']
    email = form.cleaned_data['email']
    birth_date = form.cleaned_data['birth_date']
    test_params = {
        "api_key": key,
        "country":["United States"],
        "first_name": [first_name],
        "middle_name": [middle_name],
        "last_name": [last_name],
        "strees_address": [address],
        "locality": [city],
        "region":[state],
        "postal_code":[postal_code],
        "phone": [phone],
        "email":[email],
        "birth_date":[birth_date],
    }

    json_response = requests.get(rq_url,  params=test_params).json()
    return json_response

def get_list(a):
    if a:
        response = a[0].title()
    else:
        response = None
    return response

def set_title(a):
    if a is None:
        response = None
    else:
        response = a.title()
    return response

def check_if_any(list):
    if any([not bool(item) for item in list]):
        return 0
    else: 
        return 1
    
def parse_person(json_response):
    status = json_response['status']

    if status in [404,400]:
        person_clean = {
            "status" : status,
            "error" : json_response['error'],
        }

    if status == 200:
        person_details = json_response['data']
        school_count = len(person_details['education'])
        facebook_id = person_details['facebook_id']
        fb_key = "643286449673767|3BW8OSQfjmlb6EP1fy055lVZ9pE"

        # check if any social media details are listed 
        social_media_counter = 0
        if person_details['facebook_url']: 
            social_media_counter += 1 
        if person_details['linkedin_url']: 
            social_media_counter += 1 
        if person_details['twitter_url']: 
            social_media_counter += 1 

        person_clean = {
            "status" : status,
            "record_id": person_details['id'],

        
            "social_media_counter": social_media_counter,
            
            # Demographics
            "age": person_details['birth_year'],
            "person_full_name": person_details['full_name'].title(),
            
            # Social profiles
            "facebook_url": person_details['facebook_url'],
            "facebook_id": person_details['facebook_id'],
            "linkedin_url": person_details['linkedin_url'],
            "twitter_url": person_details['twitter_url'],
            
            # Work details
            "job_title": set_title(person_details['job_title']),
            "job_company_name": set_title(person_details['job_company_name']),
            "job_company_url": person_details['job_company_website'],
            "industry": set_title(person_details['industry']),
        }
        
        ## Parse phone numbers
        phone_list = []
        
        # Response stores phone numbers in 2 sections. Function below extracts the main phone #.
        if 'mobile_phone' in person_details:
            if str(person_details['mobile_phone']) != 'null':
                phone_list.append(person_details['mobile_phone'])
            
        # Add phone numbers from the long list
        if 'phone_numbers' in person_details:
            phone_count = len(person_details['phone_numbers'])
            if phone_count > 0:
                for i in range(phone_count):
                    phone_list.append(person_details['phone_numbers'][i])
                
        # Deduplicates phone list
        phone_list = list(set(phone_list))
        # Removes weird values
        if 'None' in phone_list: phone_list.remove('None')
        if '' in phone_list: phone_list.remove('')
        phone_list = list(filter(None, phone_list))
        person_clean['phones'] = phone_list
        
        ## Parse emails
        email_list = []
        if 'work_email' in person_details:
            if str(person_details['work_email']) != 'None':
                email_list.append(person_details['work_email'])
        if 'personal_emails' in person_details:
            email_count_personal = len(person_details['personal_emails'])
            if email_count_personal > 0:
                for i in range(email_count_personal):
                    email_list.append(person_details['personal_emails'][i])
        
        if 'emails' in person_details:
            email_count_general = len(person_details['emails'])
            if email_count_general > 0:
                for i in range(email_count_general):
                    email_list.append(person_details['emails'][i]['address'])
        
        # Deduplicates email list
        email_list = list(set(email_list))
        # Removes weird values
        if 'None' in email_list: email_list.remove('None')
        if '' in email_list: email_list.remove('')
        email_list = list(filter(None, email_list))
        person_clean['emails'] = email_list
        
        # Contact info length field used to generate phone contact details section
        # if contact details are available
        person_clean['contact_info_length'] = len(phone_list+email_list)

        
        if facebook_id:
            person_clean["fb_profile"] = f"https://graph.facebook.com/v8.0/{facebook_id}/picture?redirect=true&access_token={fb_key}"
        
        person_clean["job_any"] = check_if_any([person_clean["job_title"],person_clean["job_company_name"]])
        for n in range(school_count):
            if n == 0:
                if person_details['education'][0]['school']:
                    person_clean["school_name_1"] = set_title(person_details['education'][0]['school']['name'])
                    person_clean["school_url_1"] = person_details['education'][0]['school']['website']
                person_clean["school_gpa_1"] = person_details['education'][0]['gpa']
                person_clean["school_start1"] = person_details['education'][0]['start_date']
                person_clean["school_stop1"] = person_details['education'][0]['end_date']  
                person_clean["school_degree1"] = get_list(person_details['education'][0]['degrees'])
                person_clean["school_major1"] = get_list(person_details['education'][0]['majors'])
            if n == 1:
                if person_details['education'][1]['school']:
                    person_clean["school_name_2"] = set_title(person_details['education'][1]['school']['name'])
                    person_clean["school_url_2"] = person_details['education'][1]['school']['website']                
                person_clean["school_gpa_2"] = person_details['education'][1]['gpa']
                person_clean["school_start2"] = person_details['education'][1]['start_date']
                person_clean["school_stop2"] = person_details['education'][1]['end_date'] 
                person_clean["school_degree2"] = get_list(person_details['education'][1]['degrees'])
                person_clean["school_major2"] = get_list(person_details['education'][1]['majors'])
            if n == 2:
                if person_details['education'][2]['school']:
                    person_clean["school_name_3"] = set_title(person_details['education'][2]['school']['name'])
                    person_clean["school_url_3"] = person_details['education'][2]['school']['website']
                person_clean["school_gpa_3"] = person_details['education'][2]['gpa']
                person_clean["school_start3"] = person_details['education'][2]['start_date']
                person_clean["school_stop3"] = person_details['education'][2]['end_date'] 
                person_clean["school_degree3"] = get_list(person_details['education'][2]['degrees'])
                person_clean["school_major3"] = get_list(person_details['education'][2]['majors'])
                
    return person_clean

def check_response_status(json_response):
    status = json_response['status']
    return status