import mysql.connector
from config import db  # Make sure `db` is the correct MySQL connection

def deposit(user_id, amount):
    """
    Handle depositing funds for a user.
    """
    if amount <= 0:
        raise ValueError("Amount must be positive")

    cursor = db.cursor()
    try:
        cursor.execute(
            """INSERT INTO transactions (user_id, type, amount)
            VALUES (%s, 'deposit', %s)""",
            (user_id, amount)
        )
        db.commit()
    except mysql.connector.Error as err:
        db.rollback()
        raise
    finally:
        cursor.close()
