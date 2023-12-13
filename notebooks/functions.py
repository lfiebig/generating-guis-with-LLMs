from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage 
from langchain.schema import AIMessage
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
import pandas as pd
import os
import base64
import requests

load_dotenv()

OUTPUT_FOLDER = "../generated_GUIs/"

IMAGE_INPUT_FOLDER = "../data/s2w_sample1/"


def encode_image(id):
    image_path = IMAGE_INPUT_FOLDER + f"{id}.jpg"
    print(image_path)
    with open(image_path,"rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')    
    
def describe_image(id):
    api_key = os.getenv("OPENAI_API_KEY")
    base64_image = encode_image(id)

    print(base64_image)

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    payload = {
        "model": "gpt-4-vision-preview",
        "messages": [
        {
            "role": "user",
            "content": [
            {
                "type": "text",
                "text": "given a screen, summarize its purpose briefly"
            },
            {
                "type": "image_url",
                "image_url": {
                "url": f"data:image/jpeg;base64,{base64_image}"
                }
            }
            ]
        }
        ],
        "max_tokens": 300
    }
    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
    return response