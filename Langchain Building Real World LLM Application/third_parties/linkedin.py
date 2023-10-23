import os
import requests


def scrape_linkedin(linkdin_url: str):
    #this will take information from lindedin profile and scrape/store it in variable as input to openai
    #we will do some basic ML to help decide exact which linkdin url is to be chosen
    """scrape information from LinkedIn profiles, Manually Scrape the information from the Linkedin Profile"""
    
    api_endpoint = "https://nubela.co/proxycurl/api/v2/linkedin" # as per documentation on ProxyCurl this is updated api_endpoint
    header_dic = {"Authorization": f'Bearer {os.environ.get("PROXYCURL_API_KEY")}'}

    
    response = requests.get(api_endpoint, params={"url":linkdin_url}, headers=header_dic)
    #print(response.json())
    data = response.json()
    data={
        k:v
        for k,v in data.items()
        if v not in ([],"",None)
            and k not in ["people_also_viewed","similarly_named_profiles","activities","volunteer_work","education","accomplishments","languages"] # previously only "people also viewd was removed now removing certifications as well coz message size is going over 4097 tokens"
    }    
    if data.get("groups"):
        for group_dict in data.get("groups"):
            group_dict.pop("profile_pic_url")
    
    #print(data)
    return data