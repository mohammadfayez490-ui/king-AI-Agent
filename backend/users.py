from database import get_connection


def get_all_users():
    connection = get_connection()

    users = connection.execute(
        "SELECT id, username, email FROM users"
    ).fetchall()

    connection.close()

    return [dict(user) for user in users]


def get_user_by_id(user_id):
    connection = get_connection()

    user = connection.execute(
        "SELECT id, username, email FROM users WHERE id = ?",
        (user_id,)
    ).fetchone()

    connection.close()

    if user:
        return dict(user)

    return None
