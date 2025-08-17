# database.py
import mysql.connector
from config import DB_HOST, DB_USER, DB_PASSWORD, DB_NAME

def get_db_connection():
    """Establishes a connection to the database."""
    return mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )

def setup_database():
    """Creates the necessary tables if they don't exist."""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id BIGINT PRIMARY KEY,
            username VARCHAR(255),
            first_name VARCHAR(255),
            balance INT DEFAULT 0,
            pending_balance INT DEFAULT 0,
            withdrawable_balance INT DEFAULT 0,
            referred_by BIGINT,
            daily_earnings INT DEFAULT 0,
            last_earning_date DATE,
            is_blocked BOOLEAN DEFAULT FALSE
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS withdrawals (
            id INT AUTO_INCREMENT PRIMARY KEY,
            user_id BIGINT,
            bkash_number VARCHAR(20),
            coin_amount INT,
            taka_amount FLOAT,
            status VARCHAR(20) DEFAULT 'pending',
            request_date DATETIME DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
    """)
    conn.commit()
    cursor.close()
    conn.close()

# You will need to add more functions here to:
# - create_user
# - get_user
# - update_balance
# - create_withdrawal_request
# - get_user_stats
# - etc.
