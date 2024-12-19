from flask import Flask, request, jsonify, session
from flask_bcrypt import Bcrypt
from pymongo import MongoClient
from blackjack import Blackjack

app = Flask(__name__)
app.secret_key = "your_secret_key"  # Change this to a secure key
bcrypt = Bcrypt(app)

# MongoDB setup
client = MongoClient("mongodb://localhost:27017/")
db = client['blackjack_db']
users_collection = db['users']

# Routes
@app.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data['username']
    password = data['password']

    if users_collection.find_one({'username': username}):
        return jsonify({"error": "User already exists"}), 400

    hashed_pw = bcrypt.generate_password_hash(password).decode('utf-8')
    users_collection.insert_one({'username': username, 'password': hashed_pw})
    return jsonify({"message": "User registered successfully"}), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data['username']
    password = data['password']

    user = users_collection.find_one({'username': username})
    if not user or not bcrypt.check_password_hash(user['password'], password):
        return jsonify({"error": "Invalid credentials"}), 401

    session['user'] = username
    return jsonify({"message": "Logged in successfully"}), 200

@app.route('/logout', methods=['POST'])
def logout():
    session.pop('user', None)
    return jsonify({"message": "Logged out successfully"}), 200

@app.route('/play', methods=['POST'])
def play():
    if 'user' not in session:
        return jsonify({"error": "Unauthorized"}), 401

    game = Blackjack()
    result = game.play(request.json.get("action", "hit"))  # 'hit' or 'stand'
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
