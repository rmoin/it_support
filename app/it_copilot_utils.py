# Agent class
### responsbility definition: expertise, scope, conversation script, style 
import openai
import os
from pathlib import Path  
import json
import time
from azure.search.documents.models import Vector  
import uuid
from tenacity import retry, wait_random_exponential, stop_after_attempt  

from dotenv import load_dotenv
from azure.core.credentials import AzureKeyCredential  
from azure.search.documents import SearchClient  
from openai.embeddings_utils import get_embedding, cosine_similarity
import inspect
env_path = Path('..') / 'secrets.env'
load_dotenv(dotenv_path=env_path)
openai.api_key =  os.environ.get("AZURE_OPENAI_API_KEY")
openai.api_base =  os.environ.get("AZURE_OPENAI_ENDPOINT")
openai.api_type = "azure"
import sys
import random
sys.path.append("..")
from utils import Agent, Smart_Agent, check_args, search_knowledgebase


    



PERSONA = """
You are Maya, a technical support specialist responsible for answering questions about IT & Network Setup from user and handling networking configuration updates.
You start the conversation by validating the identity of the user. Do not proceed until you have validated the identity of the user.
When you are asked with a question, use the search tool to find relavent knowlege articles to create the answer.
Answer ONLY with the facts from the search tool. If there isn't enough information, say you don't know. Do not generate answers that don't use the sources below. If asking a clarifying question to the user would help, ask the question.
Each source has a name followed by colon and the actual information, always include the source name for each fact you use in the response. Use square brakets to reference the source, e.g. [info1.txt]. Don't combine sources, list each source separately, e.g. [info1.txt][info2.pdf].
When employee request updating basic networking configuration, interact with them to get their new details.  If they don't provide new country, check if it's still United States. Make sure you have all information then use update basic config tool provided to update in the system. 
For all other information update requests, log a ticket to the IT team to update the information.
If the employee is asking for information that is not related to IT or Network, say it's not your area of expertise.
"""

def validate_identity(user_id, user_name):
    if user_id in ["1234","5678"]:
        return f"User {user_name} with id {user_id} is validated in this conversation"
    else:
        return "This user id is not valid"
def update_config(vlan_name, ipaddress, port, status):
    return f"Configuration of network {vlan_name} has been updated to {ipaddress}, {port}, {status}"
def create_ticket(user_id, updates):
    return f"A ticket number 1233445 has been created for user {user_id} with the following updates: {updates}"

AVAILABLE_FUNCTIONS = {
            "search_knowledgebase": search_knowledgebase,
            "validate_identity": validate_identity,
            "update_config": update_config,
            "create_ticket": create_ticket,

        } 

FUNCTIONS_SPEC= [  
    {
        "name": "search_knowledgebase",
        "description": "Searches the knowledge base for an answer to the IT/Network question",
        "parameters": {
            "type": "object",
            "properties": {
                "search_query": {
                    "type": "string",
                    "description": "The search query to use to search the knowledge base"
                }
            },
            "required": ["search_query"],
        },
    },
    {
        "name": "validate_identity",
        "description": "validates the identity of the user",
        "parameters": {
            "type": "object",
            "properties": {
                "user_id": {
                    "type": "string",
                    "description": "The user id to validate"
                },
                "user_name": {
                    "type": "string",
                    "description": "The user id to validate"
                }

            },
            "required": ["user_id", "user_name"],
        },

    },
    {
        "name": "update_config",
        "description": "Update the configuration of the network",
        "parameters": {
            "type": "object",
            "properties": {
                "vlan_name": {
                    "type": "string",
                    "description": "The vlan name to validate"
                },
                "ipaddress": {
                    "type": "string",
                    "description": "The new ip address to update"
                },
                "port": {
                    "type": "string",
                    "description": "The new port to update"
                },
                "status": {
                    "type": "string",
                    "description": "The new status to update"
                }
            },
            "required": ["vlan_name","ipaddress", "port", "status"],
        },

    },
    {
        "name": "create_ticket",
        "description": "Create a support ticket for the user to update advanced networking configuration other than basic",
        "parameters": {
            "type": "object",
            "properties": {
                "user_id": {
                    "type": "string",
                    "description": "The user id to validate"
                },
                "updates": {
                    "type": "string",
                    "description": "The new/changed information to update"
                }

            },
            "required": ["user_id","updates"],
        },

    },

]  


