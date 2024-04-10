##
```
What is Flask?
Flask is a micro web framework for Python based on Werkzeug and Jinja2.

What are the features of Flask?
Flask is lightweight, easy to use, and flexible.
It has built-in development server and debugger.
Flask supports extensions for adding additional functionalities.
It uses Jinja2 templating engine for rendering HTML pages.
Flask is WSGI compliant and can be deployed on various web servers.

What is the difference between Flask and Django?
Flask is a micro-framework, providing the basic functionality to build a web application. It's flexible and allows developers to choose components.
Django is a full-stack framework, providing everything needed to build a web application out-of-the-box. It follows the "batteries-included" philosophy.

What is a Flask Blueprint?
Flask Blueprints are a way to organize a Flask application into smaller and reusable components. They help in modularizing the application and structuring codebase.


How do you create a Flask application?
You create a Flask application by creating an instance of the Flask class:
python
Copy code
from flask import Flask
app = Flask(__name__)

What is a route in Flask?
A route in Flask maps a URL to a view function. It defines how Flask should respond to HTTP requests for a particular URL.

How do you define a route in Flask?
You define a route in Flask using the route() decorator, specifying the URL pattern:
python
Copy code
@app.route('/')
def index():
    return 'Hello, World!'

What is Flask-WTF?
Flask-WTF is an extension for Flask that integrates Flask with the WTForms library, which simplifies the creation and handling of web forms in Flask applications.

How do you handle forms in Flask?
You can handle forms in Flask using Flask-WTF or by manually parsing form data from request objects. Flask-WTF provides convenient features for form creation, validation, and rendering.

How do you deploy a Flask application?
Flask applications can be deployed using various methods, including standalone WSGI servers like Gunicorn or uWSGI, or by integrating with web servers like Apache or Nginx using WSGI adapters.

What is Flask-SQLAlchemy?

Flask-SQLAlchemy is an extension for Flask that integrates SQLAlchemy, a powerful Object-Relational Mapping (ORM) library, with Flask applications. It simplifies database operations and allows developers to work with databases using Python objects.
How do you set up a database connection in Flask?

You set up a database connection in Flask by configuring a database URI in your Flask application configuration. Then, you initialize a SQLAlchemy object with your Flask application and bind it to the database URI.
What is Flask-Migrate?

Flask-Migrate is an extension for Flask that integrates Alembic, a database migration tool, with Flask-SQLAlchemy. It allows developers to manage database schema changes and migrations in Flask applications conveniently.
Explain Flask's request-response cycle.

In Flask, when a request is received from a client, it goes through the request-response cycle. Flask matches the URL of the request to a view function registered with an appropriate route. The view function processes the request, optionally accessing data from the request object, and returns a response. The response can be a string, a rendered template, or a redirect to another URL.
How do you handle static files (e.g., CSS, JavaScript) in Flask?

You handle static files in Flask by placing them in a directory called static within your Flask application directory. Flask automatically serves static files from this directory when requested by clients. You can link to these static files in your templates using the url_for() function.
What is Flask-Login?

Flask-Login is an extension for Flask that provides user session management and authentication functionality. It simplifies tasks such as user login, logout, and session management in Flask applications.
How do you handle authentication in Flask?

Authentication in Flask can be handled using Flask-Login or by implementing custom authentication logic. Flask-Login provides decorators and utility functions to manage user authentication, while custom authentication logic involves validating user credentials and managing user sessions manually.
What are Flask extensions?

Flask extensions are third-party packages that integrate additional functionality with Flask applications. They provide pre-written code to handle common tasks, such as database integration, form validation, authentication, etc., making it easier to extend the functionality of Flask applications.
Explain Flask's application context and request context.

Flask uses application context and request context to manage the state of the application and the request being processed, respectively. The application context represents the state of the Flask application, while the request context represents the state of the current request being processed. Flask provides current_app and request objects to access the application and request contexts, respectively.
What is Flask-RESTful?

Flask-RESTful is an extension for Flask that simplifies the development of RESTful APIs in Flask applications. It provides features such as request parsing, response formatting, and resource routing, making it easier to build RESTful APIs with Flask.

```
