export AZURE_STORAGE_ACCOUNT=stgitcopilot
export AZURE_STORAGE_KEY=
export AZURE_STORAGE_CONTAINER=content1
export AZURE_SEARCH_SERVICE=schitcopilot
export AZURE_OPENAI_SERVICE=aoaieast
export AZURE_OPENAI_KEY=
export AZURE_OPENAI_EMB_DEPLOYMENT=text-embedding-ada-002
export AZURE_FORMRECOGNIZER_RESOURCE_GROUP=openai_east_rg
export AZURE_FORMRECOGNIZER_SERVICE=dstk-rag
export AZURE_FORMRECOGNIZER_KEY=
export AZURE_TENANT_ID=
export AZURE_SEARCH_ADMIN_KEY=
export AZURE_SEARCH_INDEX_NAME=itcopilotindex

python prepdocs.py 7520_ds.pdf --storageaccount "$AZURE_STORAGE_ACCOUNT" --storagekey "$AZURE_STORAGE_KEY" --container "$AZURE_STORAGE_CONTAINER" --searchservice "$AZURE_SEARCH_SERVICE" --openaiservice "$AZURE_OPENAI_SERVICE" --openaideployment "$AZURE_OPENAI_EMB_DEPLOYMENT" --openaikey "$AZURE_OPENAI_KEY" --searchkey "$AZURE_SEARCH_ADMIN_KEY" --index "$AZURE_SEARCH_INDEX_NAME" --formrecognizerservice "$AZURE_FORMRECOGNIZER_SERVICE" --formrecognizerkey "$AZURE_FORMRECOGNIZER_KEY" -v