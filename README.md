## flask
## Source: https://github.com/miguelgrinberg/microblog/tree/v0.1
## Code: https://github.com/miguelgrinberg/microblog
## Blueprint - https://www.youtube.com/watch?v=pjVhrIJFUEs&t=2s
## Flask Functions
## API - 
## JWT - https://www.youtube.com/watch?v=J5bIPtEbS0Q
## Pizza app - https://www.youtube.com/watch?v=aCwsQ0vUEk0&t=4120s
export FLASK_DEBUG=1
set FLASK_DEBUG=1
```
Blueprint 
Config 
Flask 
Request 
Response 
__builtins__ 
__cached__ 
__doc__
__file__ 
__getattr__
__loader__ 
__name__
__package__
__path__ 
__spec__ 
abort
after_this_request
annotations
app
appcontext_popped 
appcontext_pushed 
appcontext_tearing_down 
before_render_template 
blueprints 
cli
config 
copy_current_request_context 
ctx 
current_app 
flash 
g 
get_flashed_messages
get_template_attribute 
globals 
got_request_exception
has_app_context
has_request_context
helpers
json
jsonify 
logging, 
make_response, 
message_flashed,
redirect,
render_template
render_template_string
request 
request_finished 
request_started 
request_tearing_down 
sansio 
send_file
send_from_directory
session 
sessions 
signals 
stream_template
stream_template_string
stream_with_context
t 
template_rendered
templating 
typing 
url_for
wrappers
```
## Important Modules
```
from flask import Flask, Blueprint, jsonify, request
import auth
import threading
import pymongo
from dotenv import load_dotenv
from functools import wraps
from jose import jwt
import requests
import logging
from helper.get_blob_data import BlobStorageHandler
from langchain.embeddings import OpenAIEmbeddings
from config import Config
from langchain.schema import Document
from typing import List, Optional
import logging
from pathlib import Path
from langchain.vectorstores import Milvus
from helper.parse_unstructure import PDFParser
from helper.retriever import RetrieverInitializer
import json
from langchain.schema import Document
from langchain.vectorstores import Chroma
import chromadb
from azure.storage.blob import BlobServiceClient  
import base64
from langchain_core.messages import HumanMessage
from langchain.chat_models import AzureChatOpenAI
from langchain.document_loaders import TextLoader
from langchain.schema import Document
from langchain.retrievers import ParentDocumentRetriever  
from langchain_community.storage import MongoDBStore
from langchain.text_splitter import RecursiveCharacterTextSplitter
from config import Config
import os
import json
from bs4 import BeautifulSoup
from tabulate import tabulate
from pathlib import Path
import time
import logging
import pdf2image  
from PIL import Image
from pydantic import BaseModel, validator  
from typing import List
import shutil
import threading
import traceback
import uuid
from dataclasses import dataclass
from typing import Optional
from datetime import datetime
from enum import Enum
```



















