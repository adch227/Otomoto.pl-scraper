import mysql.connector

class MySQLHandler:
    def __init__(self, db_config):
        self.db_config = db_config
        self.conn = None
        self.cursor = None
        self.connect()

    def connect(self):
        try:
            self.conn = mysql.connector.connect(**self.db_config)
            self.cursor = self.conn.cursor()
            self.create_table()
        except mysql.connector.Error as e:
            print(f"Błąd podczas łączenia z MySQL: {e}")

    def create_table(self):
        sql = """
            CREATE TABLE IF NOT EXISTS otomoto_cars (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255),
                engine VARCHAR(50),
                power VARCHAR(50),
                details TEXT,
                price VARCHAR(50),
                mileage VARCHAR(50),
                fuel VARCHAR(50),
                gearbox VARCHAR(50),
                year VARCHAR(50),
                UNIQUE(name, price, mileage)
            )
        """
        self.cursor.execute(sql)
        self.conn.commit()

    def insert_data(self, data):
        sql = """
            INSERT IGNORE INTO otomoto_cars (name, engine, power, details, price, mileage, fuel, gearbox, year)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        for row in data:
            self.cursor.execute(sql, (
                row["Name"], row["Engine"], row["Power"], row["Details"],
                row["Price"], row["Mileage"], row["Fuel"], row["Gearbox"], row["Year"]
            ))
        
        self.conn.commit()
        print("Dane zapisane do MySQL")

    def close_connection(self):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()
