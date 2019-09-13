import xlrd
from sqlalchemy import create_engine
from openpyxl import load_workbook
from sqlalchemy import select
import pandas as pd
from pandas.io import sql
from mysql.connector import MySQLConnection
#data = load_workbook('StudentSheet.xlsx')
#table = data.get_sheet_by_name('Sheet1')
#df = pd.DataFrame(table.values)
df = pd.read_excel('StudentSheet.xlsx', sheetname='Sheet1')
print df
df['TotalMarks']=df.apply(lambda x:x['physics']+x['chemistry'],axis=1)
print df
k =df['FirstName']
#dd = tuple(k)
print k
engine = create_engine('mysql+mysqlconnector://root:Ganta@518@127.0.0.1/mydb?charset=utf8')
connection = engine.connect()
J = connection.execute("SELECT FirstName FROM mydb.user_info")
i=0
d=[]
b = []

for row in J:
         d.append(row)

print d
#for p in cc:
 #   for q in dd :
  #      if (p == q) :
   #         print p
    #        a = connection.execute("SELECT Email FROM mydb.user_info where FirstName IN p ")
     #       b.append(a)
#print b
#df['Email'] = d
#print df
   # print (row['Email'])
   # d = [row['Email']]
 # s = pd.Series(row['Email'],index=[i])
#print d
