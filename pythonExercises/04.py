"""
Using the attached orders.txt file, please write a script
that reads the file into a dictionary.  Once the file has been
read, please prepend the prefix of ‘USEQ:’ to each symbol. E.g. USEQ:MSFT.

Finally, please print the following details only for Buy orders.

OrderId, Side, (updated) Symbol, ExecQty, ExecPrice

"""
import pandas as pd

df = pd.read_csv('../Trading Ops homework_assignment (1)/orders.txt')

tmp_list = []
for word in df[' Symbol']:
    word = word.replace(" ", "")
    word = 'USEQ:' + word
    tmp_list.append(word)

df[' Symbol'] = tmp_list

df = df[df[' Side'] == 'Buy']
file = open('../Trading Ops homework_assignment (1)/ordersCorrected.txt', 'w')
df.to_csv(file)
# file created
# print information
print(df)

