import os
import pymysql
from pymysql.err import MySQLError
from dotenv import load_dotenv

load_dotenv()

_connection = None
_current_user = None
_current_user_id = None


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


def save_prediction_result(result):
    'save data for db for a user'

def get_saved_results(user_id):
    'retreive data from db for a user'
    cursor = None
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
                       SELECT name, personality_type, confidence_level, relationship_behavior
                       FROM results
                       WHERE user_id = %s
                       ORDER BY saved_on DESC
                       """, (user_id,))
        results = cursor.fetchall()
        return results
    except MySQLError as e:
        print("Error fetching saved results:", e)
        return []
    finally:
        if cursor:
            cursor.close()

