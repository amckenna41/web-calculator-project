
# Main app for multiply microservice for web calcultor #

#import python modules and dependancies
from flask import Flask
from flask import request
from flask import jsonify
from mult import *
#import flask_cors to implement CORS
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
CORS(app, support_credentials=True)

#python multiply microservice
@app.route("/")
@cross_origin(supports_credentials=True)
def mult_app():

        #get x and y header arguments
        x_string = request.args.get('x')
        y_string = request.args.get('y')

        #if no x and y arguments are input then return default values
        if (x_string == None) or (y_string == None):
                x = 0
                y = 0
                mult_value = 0
                return jsonify({"Default Value1" : x, "Default Value2" : y, "answer" : mult_value})

        #convert x and y string args to int
        x = int(x_string)
        y = int(y_string)

        #calculate multiply value of x and y
        mult_value = multiply(x,y)

        #return json object
        return jsonify({"Value1" : x, "Value2" : y, "answer" : mult_value})


#main function. Run on port 5000
if __name__ =='__main__':
    app.run(host='0.0.0.0', port = 5000, debug = True)
