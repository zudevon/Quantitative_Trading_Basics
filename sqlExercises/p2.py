import sqlite3

conn = sqlite3.connect('orders')
c = conn.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS orders(OrderId INTEGER  NOT NULL PRIMARY KEY , CreateTime VARCHAR(20) NOT NULL, Side VARCHAR(4) NOT NULL, Symbol VARCHAR(5) NOT NULL, ExecQty INTEGER  NOT NULL, ExecPrice NUMERIC(7,2) NOT NULL)')


def data_entry():
    c.execute("INSERT INTO orders VALUES(1,'2017-10-03 15:11:01','Buy','MSFT',20000,74.30)")
    c.execute("INSERT INTO orders VALUES(2,'2017-10-03 15:11:02','Sell','MSFT',100,74.20)")
    c.execute("INSERT INTO orders VALUES(3,'2017-10-03 15:11:03','Buy','GOOG',1100,954.87)")
    c.execute("INSERT INTO orders VALUES(4,'2017-10-03 15:11:04','Sell','GOOG',1500,954.87)")
    c.execute("INSERT INTO orders VALUES(5,'2017-10-03 15:11:05','Buy','YHOO',500,67.70)")
    c.execute("INSERT INTO orders VALUES(6,'2017-10-03 15:11:06','Buy','SIRI',12000,5.58)")

    conn.commit()
    c.close()
    conn.close()

create_table()
data_entry()