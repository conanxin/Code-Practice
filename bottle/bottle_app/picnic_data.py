import sqlite3
db = sqlite3.connect('picnic.db')
db.execute("CREATE TABLE picnic (id INTEGER PRIMARY KEY, item CHAR(100) NOT NULL, quant INTEGER NOT NULL)")
db.execute("INSERT INTO picnic (item,quant) VALUTES ('bread', 4)")
db.execute("INSERT INTO picnic (item,quant) VALUTES ('cheese', 2)")
db.execute("INSERT INTO picnic (item,quant) VALUTES ('grapes', 30)")
db.execute("INSERT INTO picnic (item,quant) VALUTES ('cake', 1)")
db.execute("INSERT INTO picnic (item,quant) VALUTES ('soda', 4)")
db.commit()