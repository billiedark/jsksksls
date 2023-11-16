import sqlite3


class Database:
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()

    def user_create(self, user_id, username):
        self.cursor.execute("INSERT INTO `users` (`user_id`, `username`) VALUES (?, ?)", (user_id, username))
        self.connection.commit()

    def user_exists(self, user_id):
        self.cursor.execute("SELECT user_id FROM users WHERE user_id =?", (user_id,))
        return self.cursor.fetchone() is not None