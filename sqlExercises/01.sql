CREATE TABLE executions(
   Id         INTEGER  NOT NULL PRIMARY KEY
  ,OrderId    INTEGER  NOT NULL
  ,CreateTime VARCHAR(19) NOT NULL
  ,Side       VARCHAR(4) NOT NULL
  ,Symbol     VARCHAR(4) NOT NULL
  ,ExecQty    INTEGER  NOT NULL
  ,ExecPrice  NUMERIC(6,2) NOT NULL
);

INSERT INTO executions(Id,OrderId,CreateTime,Side,Symbol,ExecQty,ExecPrice) VALUES (1,1,'2017-10-03 15:12:01','Buy','MSFT',100,74.24);
INSERT INTO executions(Id,OrderId,CreateTime,Side,Symbol,ExecQty,ExecPrice) VALUES (2,2,'2017-10-03 15:12:02','Sell','MSFT',100,74.24);
INSERT INTO executions(Id,OrderId,CreateTime,Side,Symbol,ExecQty,ExecPrice) VALUES (3,1,'2017-10-03 15:12:03','Buy','MSFT',100,74.25);
INSERT INTO executions(Id,OrderId,CreateTime,Side,Symbol,ExecQty,ExecPrice) VALUES (4,1,'2017-10-03 15:12:04','Buy','MSFT',1000,74.26);
INSERT INTO executions(Id,OrderId,CreateTime,Side,Symbol,ExecQty,ExecPrice) VALUES (5,3,'2017-10-03 15:12:05','Buy','GOOG',100,954.90);
INSERT INTO executions(Id,OrderId,CreateTime,Side,Symbol,ExecQty,ExecPrice) VALUES (6,4,'2017-10-03 15:12:06','Sell','GOOG',100,954.89);
INSERT INTO executions(Id,OrderId,CreateTime,Side,Symbol,ExecQty,ExecPrice) VALUES (7,4,'2017-10-03 15:12:07','Sell','GOOG',1200,954.81);
INSERT INTO executions(Id,OrderId,CreateTime,Side,Symbol,ExecQty,ExecPrice) VALUES (8,3,'2017-10-03 15:12:08','Buy','GOOG',1000,954.80);
INSERT INTO executions(Id,OrderId,CreateTime,Side,Symbol,ExecQty,ExecPrice) VALUES (9,5,'2017-10-03 15:12:08','Buy','YHOO',300,67.7);
INSERT INTO executions(Id,OrderId,CreateTime,Side,Symbol,ExecQty,ExecPrice) VALUES (10,6,'2017-10-03 15:12:08','Buy','SIRI',300,5.58);
INSERT INTO executions(Id,OrderId,CreateTime,Side,Symbol,ExecQty,ExecPrice) VALUES (11,6,'2017-10-03 15:12:08','Buy','SIRI',9000,5.59);

CREATE TABLE orders(
   OrderId    INTEGER  NOT NULL PRIMARY KEY
  ,CreateTime VARCHAR(20) NOT NULL
  ,Side       VARCHAR(4) NOT NULL
  ,Symbol     VARCHAR(5) NOT NULL
  ,ExecQty    INTEGER  NOT NULL
  ,ExecPrice  NUMERIC(7,2) NOT NULL
);
INSERT INTO orders(OrderId,CreateTime,Side,Symbol,ExecQty,ExecPrice) VALUES (1,'2017-10-03 15:11:01','Buy','MSFT',20000,74.30);
INSERT INTO orders(OrderId,CreateTime,Side,Symbol,ExecQty,ExecPrice) VALUES (2,'2017-10-03 15:11:02','Sell','MSFT',100,74.20);
INSERT INTO orders(OrderId,CreateTime,Side,Symbol,ExecQty,ExecPrice) VALUES (3,'2017-10-03 15:11:03','Buy','GOOG',1100,954.87);
INSERT INTO orders(OrderId,CreateTime,Side,Symbol,ExecQty,ExecPrice) VALUES (4,'2017-10-03 15:11:04','Sell','GOOG',1500,954.87);
INSERT INTO orders(OrderId,CreateTime,Side,Symbol,ExecQty,ExecPrice) VALUES (5,'2017-10-03 15:11:05','Buy','YHOO',500,67.70);
INSERT INTO orders(OrderId,CreateTime,Side,Symbol,ExecQty,ExecPrice) VALUES (6,'2017-10-03 15:11:06','Buy','SIRI',12000,5.58);

SELECT Symbol, COUNT(Symbol),SUM(ExecQty) AS 'TotalQty' FROM executions GROUP BY Symbol