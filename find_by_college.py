# here i will be finding the hackathon name by the college
from fastapi import FastAPI
from fastapi import Request
app=FastAPI()
import json
from fastapi.responses import JSONResponse
from get_hack_name_by_path import return_the_hackathon
@app.get("/")

async def root():
    return{'message':'HelloWorld'}
@app.post("/")
async def handle_request(request:Request):
    payload=await request.json()
    intent=payload['queryResult']['intent']['displayName']
    parameters=payload['queryResult']['parameters']['university']
    if intent=='find_hackathon_by_college':
        returned=return_the_hackathon('universities.json',parameters)
        return JSONResponse(
            content={
                'fulfillmentText':f"I found the {len(returned)} hackathon(s) corresponding to {parameters} which are {', '.join(returned)}"  
            }
        )