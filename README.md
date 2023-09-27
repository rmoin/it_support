# Instructions
1. Create an Azure OpenAI deployment in an Azure subscription with a GPT-35-Turbo deployment
1. Create a `secrets.env` file in the root of this folder
    ```txt
AZURE_OPENAI_ENDPOINT="" 
AZURE_OPENAI_API_KEY=""
AZURE_OPENAI_EMB_DEPLOYMENT=""
AZURE_OPENAI_CHAT_DEPLOYMENT=""
USE_AZCS="True" #if false, it will use the Faiss library for search
AZURE_SEARCH_SERVICE_ENDPOINT=""
AZURE_SEARCH_INDEX_NAME=
CACHE_INDEX_NAME="YOUR_SEARCH_INDEX_NAME" #optional, required when USE_SEMANTIC_CACHE="True"
AZURE_SEARCH_ADMIN_KEY=
AZURE_OPENAI_API_VERSION="2023-07-01-preview"
USE_SEMANTIC_CACHE="False" #set to True if use semantic Cache.
SEMANTIC_HIT_THRESHOLD=0.9 #Threshold in similarity score to determine if sematic cached will be used
    ```
1. Create a python environment
1. Import the requirements.txt `pip install -r requirements.txt`
1. From the window, run `streamlit run it_copilot.py`