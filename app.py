from flask import Flask, jsonify, request
from models import User, db
import os

# Load environment variables


app = Flask(__name__)

# App configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1234@localhost:5432/restapi'


# Initialize extensions
db.init_app(app)


# Exception Handling
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found', 'message': 'The requested URL was not found on the server'}), 404

# Login route to generate JWT tokens
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    # Simulating user authentication (replace with a database query in production)
    
# Retrieve all users (protected route)
@app.route('/users', methods=['GET'])
def users():
    # Retrieve the current logged-in user's ID
    users = User.query.all()
    return jsonify([user.to_dict() for user in users]), 200

# Add a user to the database
@app.route('/users', methods=['POST'])

def create_users():
    data = request.get_json()
    new_user = User(username=data['username'], email=data['email'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify(new_user.to_dict()), 201

# Retrieve user by ID
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get_or_404(user_id)
    return jsonify(user.to_dict()), 200

# Update user information
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    user = User.query.get_or_404(user_id)
    user.username = data['username']
    user.email = data['email']
    db.session.commit()
    return jsonify(user.to_dict()), 200

# Delete a user
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    return '', 204

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(port=5004, debug=True)

