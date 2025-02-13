from flask import Flask, jsonify, request
from flasgger import Swagger, swag_from

app = Flask(__name__)
swagger = Swagger(app)

@app.route('/api', methods=['GET'])
@swag_from({
    'responses': {
        200: {
            'description': 'A JSON object containing email and password',
            'schema': {
                'type': 'object',
                'properties': {
                    'email': {
                        'type': 'string',
                        'example': 'hello@tester.com'
                    },
                    'password': {
                        'type': 'string',
                        'example': 'hello@123'
                    }
                }
            }
        }
    }
})
def get_data():
    return jsonify({
        'email': 'hello@tester.com',
        'password': 'hello@123'
    })

@app.route('/api/user', methods=['POST'])
@swag_from({
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'email': {
                        'type': 'string',
                        'example': 'newuser@tester.com'
                    },
                    'password': {
                        'type': 'string',
                        'example': 'newpassword@123'
                    }
                }
            }
        }
    ],
    'responses': {
        201: {
            'description': 'User created successfully',
            'schema': {
                'type': 'object',
                'properties': {
                    'message': {
                        'type': 'string',
                        'example': 'User created successfully'
                    }
                }
            }
        }
    }
})
def create_user():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    # Here you would typically save the user data to a database
    return jsonify({
        'message': 'User created successfully'
        }), 201

if __name__ == '__main__':
    app.run(debug=True)