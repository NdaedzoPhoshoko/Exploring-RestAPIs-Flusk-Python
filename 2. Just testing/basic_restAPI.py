#creating a simple REST API using Flask
from flask import Flask, jsonify  # Import Flask and jsonify from the flask module

app = Flask(__name__)  # Create an instance of the Flask class

@app.route('/api', methods=['GET'])  # Define a route for the API endpoint with the GET method
def get_data():
    # Return a JSON response with email and password data
    return jsonify({
        'email': 'hello@tester.com',
        'password': 'hello@123'
    })

if __name__ == '__main__':
    app.run(debug=True)  # Run the Flask app in debug mode

# run the program output on http://127.0.0.1:5000/api
