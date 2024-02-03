from flask import *

app = Flask(__name__)


@app.route('/login', methods=['GET'])
def login():
    uname = request.args.get('uname')
    password = request.args.get('pass')
    if uname == 'admin' and password == 'admin':
        return "Welcome %s" % uname
    else:
        return "Invalid username or password" 
    
    


if __name__ == '__main__':
    app.run(debug=True)