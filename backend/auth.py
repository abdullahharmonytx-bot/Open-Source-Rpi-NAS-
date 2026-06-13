from backend.database import connect_db
from backend.security import hash_password

def admin_exists():

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT COUNT(*) FROM users WHERE role='administrator'"
    )

    count = cursor.fetchone()[0]

    conn.close()

    return count > 0


def create_admin(
    full_name,
    username,
    hash_password(password),
):

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO users
    (
        full_name,
        username,
        password,
        role
    )
    VALUES
    (?, ?, ?, ?)
    """,
    (
        full_name,
        username,
        password,
        "administrator"
    ))

    conn.commit()
    conn.close()
