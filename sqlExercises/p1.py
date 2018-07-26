import sqlite3

conn = sqlite3.connect('executions')
c = conn.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS executions(Id INTEGER  NOT NULL PRIMARY KEY ,OrderId INTEGER  NOT NULL ,CreateTime VARCHAR(19) NOT NULL, Side VARCHAR(4) NOT NULL, Symbol VARCHAR(4) NOT NULL, ExecQty INTEGER  NOT NULL, ExecPrice  NUMERIC(6,2) NOT NULL)')

def data_entry():
    c.execute("INSERT INTO executions VALUES(1,1,'2017-10-03 15:12:01','Buy','MSFT',100,74.24)")
    c.execute("INSERT INTO executions VALUES(2,2,'2017-10-03 15:12:02','Sell','MSFT',100,74.24)")
    c.execute("INSERT INTO executions VALUES(3,1,'2017-10-03 15:12:03','Buy','MSFT',100,74.25)")
    c.execute("INSERT INTO executions VALUES(4,1,'2017-10-03 15:12:04','Buy','MSFT',1000,74.26)")
    c.execute("INSERT INTO executions VALUES(5,3,'2017-10-03 15:12:05','Buy','GOOG',100,954.90)")
    c.execute("INSERT INTO executions VALUES(6,4,'2017-10-03 15:12:06','Sell','GOOG',100,954.89)")
    c.execute("INSERT INTO executions VALUES(7,4,'2017-10-03 15:12:07','Sell','GOOG',1200,954.81)")
    c.execute("INSERT INTO executions VALUES(8,3,'2017-10-03 15:12:08','Buy','GOOG',1000,954.80)")
    c.execute("INSERT INTO executions VALUES(9,5,'2017-10-03 15:12:08','Buy','YHOO',300,67.7)")
    c.execute("INSERT INTO executions VALUES(10,6,'2017-10-03 15:12:08','Buy','SIRI',300,5.58)")
    c.execute("INSERT INTO executions VALUES(11,6,'2017-10-03 15:12:08','Buy','SIRI',9000,5.59)")

    conn.commit()
    c.close()
    conn.close()

create_table()
data_entry()