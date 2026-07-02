from database import get_connection


def register_user(username, email, password):
    connection = get_connection()

    connection.execute(
        """
        INSERT INTO users (username, email, password)
        VALUES (?, ?, ?)
        """,
        (username, email, password)
    )

    connection.commit()
    connection.close()

    return {
        "success": True,
        "message": "User registered successfully."
    }


def login_user(email, password):
    connection = get_connection()

    user = connection.execute(
        """
        SELECT * FROM users
        WHERE email = ? AND password = ?
        """,
        (email, password)
    ).fetchone()

    connection.close()

    if user:
        return {
            "success": True,
            "username": user["username"]
        }

    return {
        "success": False,
        "message": "Invalid email or password."
    }
