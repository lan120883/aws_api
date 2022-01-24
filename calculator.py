from flask import Flask, jsonify
from flask_restful import Resource, Api, reqparse
app = Flask(__name__)
api = Api(app)

class Caculator(Resource):
    def get(self):
        # create request parser
        parser = reqparse.RequestParser()
        # create argument 'cal', 'x','y'
        parser.add_argument('cal', type=str)
        parser.add_argument('x', type=str)
        parser.add_argument('y', type=str)
        # parse 'name'
        cal = parser.parse_args().get('cal')
        x = int(parser.parse_args().get('x'))
        y = int(parser.parse_args().get('y'))
                # make json from greeting string
        ret = 0        
        if cal=='add':
            ret = x+y
        elif cal=='subtract':
            ret = x-y
        elif cal=='multiply':
            ret = x*y
        elif cal=='divide':
            if y != 0:
                ret = x/y   
            else:
                ret = 0      
        else:
            'Not correct'        

        return ret
# api_endpoint
api.add_resource(Caculator, '/cal',)
if __name__ == '__main__' :
    # app.run(debug=True)
    app.run(host='0.0.0.0', port=8888)

