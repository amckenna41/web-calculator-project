
#Main app for modulus function microservice in python #

#import python modules
from flask import Flask
from flask import request
from flask import jsonify
from mod import *
#import flask-cors for CORS integration
try:
    from flask_cors import CORS
    from flask_cors import cross_origin
except ImportError:
    import os
    parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    os.sys.path.insert(0, parentdir)

    from flask_cors import CORS


app = Flask(__name__)

#implement CORS
CORS(app)

#python microservice for mod function
@app.route("/")
def mod_app():

        #get x and y parameters
        x_string = request.args.get('x')
        y_string = request.args.get('y')

        #if no x and y arguments are input then return default values
        if (x_string == None) or (y_string == None):
                x = 0
                y = 0
                mod_value = 0
                return jsonify({"Default Value1" : x, "Default Value2" : y, "answer" : mod_value})

        #convert x and y parameters to int
        x = int(x_string)
        y = int(y_string)

        #call mod function on x and y
        mod_value = mod(x,y)

        #return json object
        return jsonify({"Value1" : x, "Value2" : y, "answer" : mod_value})

#main function for service, running on port 5000
if __name__ =='__main__':
    app.run(host='0.0.0.0', port = 5000, debug = True)
