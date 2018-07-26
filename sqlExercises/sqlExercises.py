import sqlite3
import pandas as pd

"""
•	Total Number of orders and executions by Symbol, sorted in ascending order.  
Output should contain the following columns – 
Symbol, # of Orders, # of Executions.  Please show all orders.

•	Total Number of shares ordered and shares executed per symbol.  
Output should contain the following columns – Symbol, Total Ordered Qty, 
Total Executed Qty, Remaining Qty, Status (Filled or Partially Filled), 
Average Price.  Please show totals for all symbols in the orders and executions tables.

•	List of symbols and side (buy/sell) that have more than 1,000 total shares 
executed by side.  Output should contain – Symbol, Side and Total Executed Qty.

"""




def sql_exercises():
    """ Create cursors for each db """
    conn_orders = sqlite3.connect('orders')
    c_orders = conn_orders.cursor()
    conn_exe = sqlite3.connect('executions')
    c_exe = conn_exe.cursor()

    """ First Exercisie """
    print('-------01')
    # c_exe.execute("SELECT * FROM executions GROUP BY Symbol ")
    c_exe.execute("SELECT Symbol, COUNT(Symbol),SUM(ExecQty) "
                  "AS 'TotalQty' FROM executions GROUP BY Symbol ")

    # for row in zip(c_exe.fetchall(), c_orders.fetchall()):
    for row in c_exe.fetchall():
        print(row)

    print('---------02')
    """ Second Exercise """
    c_exe.execute("SELECT Symbol, Side, SUM(ExecQty) "
                  "AS 'TotalQty', AVG(ExecPrice) FROM executions GROUP BY OrderId ")

    c_orders.execute("SELECT ExecQty, ExecPrice FROM orders")

    counter = 0
    temp = []
    for row in zip(c_exe.fetchall(), c_orders.fetchall()):
        temp += [(list(row[0]) + list(row[1]))]

    info_df = pd.DataFrame(temp, columns=[
        'Symbol', 'Side', 'Total_Executed_Qty', 'Avg_Exec_Price','Total_Order_Qty', 'Order_Price',  ])


    def order_filled(row):
        amt = row['Total_Order_Qty'] - row['Total_Executed_Qty']
        if amt == 0:
            result = 'Filled'
        else:
            result = 'Partially Filled'
        return result

    def remaining_qty(row):
        result = row['Total_Order_Qty'] - row['Total_Executed_Qty']
        return result

    def avg_price(row):
        result = (row['Avg_Exec_Price'] + row['Order_Price'])/2
        return result

    info_df['Remaining_Qty'] = info_df.apply(remaining_qty, axis=1)
    info_df['Status'] = info_df.apply(order_filled, axis=1)
    info_df['Avg_Price'] = info_df.apply(avg_price, axis=1)
    print(info_df)

    print('------------03')
    """ Third Exercise """
    c_exe.execute("SELECT Symbol, Side, ExecQty FROM executions " 
                  "WHERE ExecQty>=1000 ")

    for row in c_exe.fetchall():
        print(row)

sql_exercises()