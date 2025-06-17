import os
from dotenv import load_dotenv
from flask import Flask, request, jsonify
from pymongo import MongoClient
from werkzeug.security import generate_password_hash
import re
from flask_cors import CORS

load_dotenv()

app = Flask(__name__)
CORS(app) 

client = MongoClient(os.getenv("MONGO_URI"))
db = client["usuariosApp"]
usuarios = db["usuarios"]

@app.route("/")
def home():
    return "¡Hola! Esta es tu mini app de registro."

@app.route("/api/users", methods=["POST"])  
def register():
    data = request.get_json()
    print("Datos recibidos:", data)

    name = (data.get("name") or data.get("nombre") or "").strip()
    email = (data.get("email") or data.get("correo") or "").strip().lower()
    password = data.get("password", "").strip()

    if not name or not email or not password:
        print("❌ Faltan campos")
        return jsonify({"error": "Missing fields"}), 400

    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        print("❌ Email inválido")
        return jsonify({"error": "Invalid email"}), 400

    if len(password) < 6:
        print("❌ Contraseña muy corta")
        return jsonify({"error": "Password too short"}), 400

    if usuarios.find_one({"email": email}):
        print("❌ Email ya registrado")
        return jsonify({"error": "Email already registered"}), 400

    hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
    new_user = {
        "name": name,
        "email": email,
        "password": hashed_password
    }

    result = usuarios.insert_one(new_user)

    return jsonify({
        "message": "User registered successfully",
        "new_user_created": {
            "id": str(result.inserted_id),
            "name": name,
            "email": email
        }
    }), 201

if __name__ == "__main__":
    app.run(debug=True)