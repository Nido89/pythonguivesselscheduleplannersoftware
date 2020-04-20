import sqlite3


class Database:
    # initializing the database
    def __init__(self, db):
        # connecting to the databse
        self.conn = sqlite3.connect(db)
        # cursor to excute queries from databse
        self.cur = self.conn.cursor()  # connecting to the database for queries
        # sql query after setting up the cursor to create table in sqldb
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS parts(id INTEGER PRIMARY KEY,part text,customer text, retailer text,price text)")
        # setting up connection
        self.conn.commit()

# CRUD Operations
    def fetch(self):
        # execute this query below
        self.cur.execute("SELECT * FROM parts")
        # fetch all the rows
        rows = self.cur.fetchall()
        # just simple return all the rows
        return rows

    def insert(self, part, customer, retailer, price):
        # doing an insert operation in to the databse where null is  a replacement to protect from sql injections
        # and question marks are placeholders for each field when id is null
        self.cur.execute("INSERT INTO parts VALUES (NULL,?,?,?,?)",
                         (part, customer, retailer, price))
        self.conn.commit()
    # trailing comma after id because id is a tuple

    def remove(self, id):
        self.cur.execute("DELETE FROM parts WHERE id=?", (id,))
        self.conn.commit()

    def update(self, id, part, customer, retailer, price):
        self.cur.execute("UPDATE parts SET part = ?, customer = ?,retailer = ? ,price=? WHERE id=?",
                         (part, customer, retailer, price, id))
        self.conn.commit()

    # Deconstructor when all objects are deleted
    def __del__(self):
        # just closing the connection after todb
        self.conn.close()


# to instantiate databse for this file
db = Database('store.db')

# db.insert("Viking Princes", "Passenger Ferry", "Port of Turku", "4000")
# db.insert("Viking Diana", "Passenger Ferry", "Port of Helsinki", "56000")
# db.insert("Silja Princes", "Passenger Ferry", "Port of Turku", "56000")
# db.insert("Viking Serenade", "Passenger Ferry", "Port of Aland", "6000")
# db.insert("Maersk King", "Cargo Ferry", "Port of Marrakesh", "20000")
# db.insert("Maersk Loader", "Cargo Ferry", "Port of Gawadar", "8000")
# db.insert("Schenker Princes", "Cargo Ferry", "Port of Singapore", "9000")
