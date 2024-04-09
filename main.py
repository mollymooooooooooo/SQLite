import sqlite3;

con = sqlite3.connect("firstDB.db")
cursor = con.cursor()

# создаем таблицу people
cursor.execute("""CREATE TABLE IF NOT EXISTS people
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                age INTEGER,
                salary INTEGER
                )
            """)
con.commit()
# данные для добавления
data = [("Ладюша", 18, 400), ("Дилярушка", 17, 500), ("Лейладжон", 18, 500), ("Аделинаджон", 16, 1000)
        ("Элинушка", 19, 500), ("Анюша", 15, 1000), ("Эльзахон", 17, 2000), ("Амалишка", 18, 1700)
        ("Софиюша", 16, 2540), ("Каринушка", 16, 1890), ("Луизахон", 18, 2570), ("Настюша", 14, 1698)
        ("Иделиябону", 42, 2558)]
cursor.executemany("INSERT INTO people (name, age, salary) VALUES (?, ?, ?)", data)
con.commit()
