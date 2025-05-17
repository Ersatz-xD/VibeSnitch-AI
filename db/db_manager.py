import os
import pymysql
from pymysql.err import MySQLError
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Global connection and user info
_connection = None
_current_user = None
_current_user_id = None

# === User Session Management ===

def set_current_user(username, user_id):
    global _current_user, _current_user_id
    _current_user = username
    _current_user_id = user_id

def get_current_user():
    return _current_user

def get_current_user_id():
    return _current_user_id

def get_user_id(username):
    conn = get_connection()
    cursor = None
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT user_id FROM users WHERE username = %s", (username,))
        result = cursor.fetchone()
        return result['user_id'] if result else None
    except MySQLError as e:
        print("Error getting user ID:", e)
        return None
    finally:
        if cursor:
            cursor.close()

# === Connection Management ===

def get_connection():
    global _connection
    if not _connection or not _connection.open:
        try:
            print("Connecting to DB...")

            _connection = pymysql.connect(
                host=os.getenv("DB_HOST", "localhost"),
                user=os.getenv("DB_USER"),
                password=os.getenv("DB_PASSWORD"),
                database=os.getenv("DB_NAME", "vibe_snitch"),
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor
            )
        except MySQLError as e:
            print(f"MySQL Connection Error: {e}")
            raise
    return _connection

def close_connection():
    global _connection
    if _connection and _connection.open:
        _connection.close()
        _connection = None

# === Auth Functions ===

def login_user(username, password):
    cursor = None
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT user_id FROM users WHERE username=%s AND password=%s", (username, password))
        result = cursor.fetchone()
        if result is not None:
            set_current_user(username, result['user_id'])
            return True
        else:
            print("Invalid credentials")
            return False
    except MySQLError as e:
        print("Login Error:", e)
        return False
    finally:
        if cursor:
            cursor.close()

def signup_user(username, password):
    cursor = None
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT user_id FROM users WHERE username=%s", (username,))
        if cursor.fetchone():
            print("Username already exists.")
            return False
        cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
        conn.commit()
        print("User inserted.")
        return True
    except MySQLError as e:
        print("Signup Error:", e)
        return False
    finally:
        if cursor:
            cursor.close()

# === Prediction Saving and Retrieval ===

def save_prediction_result(result):
    cursor = None
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO results (
                user_id, name, personality_type, confidence_level,
                top_traits, relationship_behavior
            ) VALUES (%s, %s, %s, %s, %s, %s)
        """, (
            _current_user_id,
            result['name'],
            result['mbti_type'],
            result['confidence'],
            ', '.join(result['traits']),
            result['relationship_behavior']
        ))
        conn.commit()
    except MySQLError as e:
        print("Save Prediction Error:", e)
    finally:
        if cursor:
            cursor.close()

def get_saved_results(user_id):
    'retreive data from db for a user'
    cursor = None

