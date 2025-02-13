from flask import Flask, jsonify
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app) # this line allows us to add documentation using swagger
# it brings forth the apidocs
@app.route('/api', methods=['GET'])
def get_data():
    """
    Get user data
    ---
    responses:
      200:
        description: A JSON object containing email and password
        schema:
          type: object
          properties:
            email:
              type: string
              example: hello@tester.com
            password:
              type: string
              example: hello@123
    """
    return jsonify({
        'email': 'hello@tester.com',
        'password': 'hello@123'
    })

if __name__ == '__main__':
    app.run(debug=True)

    # run the program output on http://127.0.0.1:5000/apidocs