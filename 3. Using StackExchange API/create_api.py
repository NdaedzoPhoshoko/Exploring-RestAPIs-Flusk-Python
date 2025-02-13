'''Install:
    pip3 install flask
    pip3 install flask-sqlachemy
    pip3 freeze > requirements.txt  | folder that will store all dependencies needed to run the program
'''
from flask import Flask
app = Flask(__name__)

# create a route
@app.route('/') # we are passing data through an endpoint of the api
def index(): # the index page http://127.0.0.1:5000/ will give this endpoint if there is no endpoint specified
    return 'Hello!'

@app.route('/drinks/400') # creating another endpoint
def get_drinks():
    return {
        'drink1': 'drink 1',
        'drink2': 'drink 2',
        'drink3': 'Coke'} # this are the data that can be fetched using a GET by other developers

if __name__ == '__main__':
    app.run(debug=True)