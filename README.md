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
1. Core Flask Development
Flask-WTF: Simplifies form handling with built-in validation and CSRF protection.
Flask-SQLAlchemy: Adds ORM support to Flask for interacting with databases.
Flask-Migrate: Manages database migrations using Alembic with Flask-SQLAlchemy.
Flask-Bcrypt or Flask-Argon2: For password hashing and encryption.
Flask-Login: Handles user authentication and session management.


2. Database Interaction
SQLAlchemy: A powerful ORM for complex database interactions.
Peewee: A lightweight ORM for simpler applications.
PyMongo: For working with MongoDB.
Redis-py: For caching and session storage.


3. API Development
Flask-RESTful: Adds tools for creating REST APIs with Flask.
Flask-RESTPlus: Similar to Flask-RESTful, with added support for Swagger documentation.
Marshmallow: For object serialization and validation.
APScheduler: For running background jobs and scheduled tasks.


4. Security
Flask-Security: An extension integrating authentication, authorization, and user management.
Flask-Limiter: Implements rate limiting for API endpoints.
Flask-CORS: Enables Cross-Origin Resource Sharing for APIs.
Flask-Helmet: Provides basic security headers for Flask applications.


5. Template and Frontend Integration
Jinja2: Flask's default template engine.
WTForms: Simplifies creating and validating HTML forms.
Flask-Bootstrap or Flask-Material: For integrating frontend frameworks.

6. Testing and Debugging
Pytest: A robust framework for testing Flask applications.
Flask-Testing: Adds testing utilities specific to Flask.
Coverage.py: Measures code coverage in your tests.


7. File and Media Handling
Flask-Uploads or Flask-Storage: For file upload and storage management.
Pillow: For image processing and manipulation.
8. Task Queues and Background Jobs
Celery: For managing asynchronous tasks.
RQ (Redis Queue): A lightweight alternative for background task processing.


9. Other Useful Libraries
Dotenv: Loads environment variables from .env files.
Flask-Mail: For sending emails from your Flask application.
Flask-Caching: Adds caching support to improve performance.
Gunicorn: A WSGI server for deploying Flask apps in production.
Requests: For making HTTP requests.


10. Advanced Tools
Flask-SocketIO: Adds WebSocket support for real-time communication.
Flask-Talisman: Helps secure apps by setting HTTP headers like CSP.
Flask-Admin: Provides an administrative interface for your app.
General Recommendations:
Stay updated with Flask's official documentation and explore Flask extensions from the Flask Extension Registry. Choose libraries based on your project's requirements for a clean and efficient stack.
```
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
import asyncio

```



















