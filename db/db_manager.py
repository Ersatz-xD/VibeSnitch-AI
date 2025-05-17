import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
import os

load_dotenv()  # Loads environment variables from .env

DB_HOST = os.getenv("DB_HOST", "localhost")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME", "vibe_snitch")


current_user = {
    "user_id": None,
    "username": None
}

def connect_db():
    try:
        conn = mysql.connector.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASS
        )
        if conn.is_connected():
            return conn
    except Error as e:
        print("Connection Error:", e)
        return None


def login_user(username, password):
    try:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT id FROM users WHERE username=%s AND password=%s", (username, password))
        result = cursor.fetchone()
        if result:
            current_user['user_id'] = result[0]
            current_user['username'] = username
            return True
        return False
    except Error as e:
        print("Login Error:", e)
        return False
    finally:
        if conn.is_connected():
            conn.close()

def signup_user(username, password):
    try:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username=%s", (username,))
        if cursor.fetchone():
            return False  # Username already exists

        cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
        conn.commit()
        return True
    except Error as e:
        print("Signup Error:", e)
        return False
    finally:
        if conn.is_connected():
            conn.close()

def save_prediction_result(user_id, result):
    try:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO results (
                user_id, name, personality_type, confidence_level,
                top_traits, relationship_behavior
            )
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (
            user_id,
            result['name'],
            result['mbti_type'],
            result['confidence'],
            ', '.join(result['traits']),
            result['relationship_behavior']
        ))
        conn.commit()
    except Error as e:
        print("Save Error:", e)
    finally:
        if conn.is_connected():
            conn.close()


def get_saved_results(user_id):
    'Implement Logic to retreive saved results for a user'
