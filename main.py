from fastapi import FastAPI
from fastapi import Request
app=FastAPI()
import json
from fastapi.responses import JSONResponse
from main2 import return_the_hackathon
from main2 import return_all_the_detail
from main2 import return_only_matching_hackathon
from main2 import search_index
from main2 import get_labels
from get_live import get_live_indices
@app.get("/")

async def root():
    return{'message':'HelloWorld'}
@app.post("/")
async def handle_request(request:Request):
    payload=await request.json()
    intent=payload['queryResult']['intent']['displayName']
    if intent=='find_hackathon_by_college':
        parameters=payload['queryResult']['parameters']['university']
        returned=return_the_hackathon('universities.json',parameters)
        return JSONResponse(
            content={

                'fulfillmentText':f"I found the {len(returned)} hackathon(s) corresponding to {parameters} which are {', '.join(returned)} .You can now write find the details of hackathon_name and I will find you the details or You can also write find me details of these hackathons and I will tell the hackathon details corresponding to the college you asked"

                
            }
        )
    if intent=='hackathon_detail_finder':
        university = payload["queryResult"]["outputContexts"][0]["parameters"]["university"]
        hackathon_name=payload["queryResult"]["outputContexts"][1].get('parameters')['hackathon_name']
        if(hackathon_name):
            to_return=return_only_matching_hackathon('universities.json',university,hackathon_name)
            return JSONResponse(
                content={
                    'fulfillmentText':f"{to_return}"
                }
            )
            
        
        else:
            hack_details=return_all_the_detail('universities.json',university)
            return JSONResponse(
            
                content={
                    'fulfillmentText':f"From {university} {hack_details}"
                }
            )
    if intent=='round_details':
        # first of all I need to check ki hamara kaun sa college ki baat ho rhi hai
        university = payload["queryResult"]["outputContexts"][0]["parameters"]['university']
        hackathon_name=payload["queryResult"]["outputContexts"][0]["parameters"]["hackathon_name"]
        # Need to search the index of the corresponding university
        get_university_index=search_index('universities.json',university,hackathon_name)
        label_here=get_labels('output.json','labelss.json',get_university_index)

        return JSONResponse(
            content={
                'fulfillmentText':f"{label_here}"
            }
        )
    if intent=='live-hackathons':
        indices_of_live_dates=get_live_indices('output.json')
        with open('universities.json') as file:
            data_dict=json.load(file)
        result_keys = [list(data_dict.keys())[index] for index in indices_of_live_dates]
        # now indices_of_live m jo jo hai wo sab chaiye json m se
        return JSONResponse(
            content={
                'fulfillmentText':f"I found the following colleges in my data {', '.join(result_keys)}"
            }
        )
            