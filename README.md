## flask
## Source: https://github.com/miguelgrinberg/microblog/tree/v0.1
## Code: https://github.com/miguelgrinberg/microblog

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



















