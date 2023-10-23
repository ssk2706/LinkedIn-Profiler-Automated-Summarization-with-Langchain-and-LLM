from langchain.utilities import SerpAPIWrapper

import json

def get_profile_url(text:str):
   
   
   
   
    """Searches for Linkedin Profile Page through SerpAPI and return RAW results"""
    # params = self.get_params(text)

    search = SerpAPIWrapper()

    #res = search.run(f"{text}") # not useful as SerpAPI.py mentions that it process the result data before returning so can't use this one instead of this found a method called results that return raw data so will use that one

    res = search.results(f"{text}")
    
    #return res
    return json.dumps(res['organic_results'][0])
    # as it wasn't returning valid json trying out to covert it into json using python lib



    # search = SerpAPIWrapper()
    # result = search.run(f"{text}")
    # return result
    
    
# def results(self, query: str) -> dict:

#     """Run query through SerpAPI and return the raw result."""
    
#     params = self.get_params(query)

#     with HiddenPrints():

#         search = self.search_engine(params)

#         res = search.get_dict()

#     return res