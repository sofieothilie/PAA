import sqlite3


DB = "todos.db"


def get_connection():
    return sqlite3.connect(DB)


def init_db():
    with get_connection() as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS todos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                completed BOOLEAN NOT NULL DEFAULT 0
            )
            """
        )


def add_todo(title: str) -> str:
    with get_connection() as conn:
        conn.execute(
            "INSERT INTO todos (title) VALUES (?)",
            (title,),
        )

    return f"Added todo: {title}"


def list_todos() -> str:
    with get_connection() as conn:
        todos = conn.execute("SELECT id, title, completed FROM todos").fetchall()

    if not todos:
        return "There are no todos."

    return "\n".join(
        f"{id}. [{'x' if completed else ' '}] {title}" for id, title, completed in todos
    )
