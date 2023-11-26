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

    def category_create(self, category_name):
        self.cursor.execute("INSERT INTO `categories` (`name`) VALUES (?)", (category_name,))
        self.connection.commit()

    def create_item(self, category, name, description, stock, type, prices, img):
        self.cursor.execute(
            "INSERT INTO `items` (`category`, `name`, `description`, `stock`, `type`, `prices`, `img`) VALUES (?,?,?,?,?,?,?)",
            (category, name, description, stock, type, prices, img))
        self.connection.commit()

    def get_categories(self):
        self.cursor.execute("SELECT name FROM categories")
        return [row[0] for row in self.cursor.fetchall()]

    def get_items(self, category):
        self.cursor.execute("SELECT * FROM items WHERE category =?", (category,))
        return [row for row in self.cursor.fetchall()]

    def get_item(self, item_id):
        self.cursor.execute("SELECT * FROM items WHERE id =?", (item_id))
        return [row for row in self.cursor.fetchone()]