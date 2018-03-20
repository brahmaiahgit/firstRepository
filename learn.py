#!/usr/bin/python
import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine
from sqlalchemy.types import VARCHAR
from sqlalchemy.types import String
from pandas import ExcelWriter
from pandas import ExcelFile
from pandas.io import sql
from mysql.connector import MySQLConnection

# "con = mysql.connector.connect(
#          user='root',
#          password='Ganta@518',
#          host='127.0.0.1',
#          database='mydb')"
df = pd.read_excel('Data1.xlsx', sheet_name='Sheet1')
print df
def highlight_max(data, color='yellow'):
    '''
    highlight the maximum in a Series or DataFrame
    '''
    attr = 'background-color: {}'.format(color)
    if data.ndim == 1:  # Series from .apply(axis=0) or axis=1
        is_max = data == data.max()
        return [attr if v else '' for v in is_max]
    else:  # from .apply(axis=None)
        is_max = data == data.max().max()
        return pd.DataFrame(np.where(is_max, attr, ''),
                            index=data.index, columns=data.columns)
print df.dtypes
print df.columns
print len(df)
print df.shape
print df.ix[:,0:1]
print df['Marks2'].unique()
#print df.sort(['Name'])
print df['Name'].value_counts()
p = df.style.apply(highlight_max,subset=['Name','Marks1'])
print p
df['Marks1Slice'] = df['Marks1'].diff()
#print df['Marks1Slice']
#df[['Name','Marks1','Marks2']].plot()
#plt.show()
'''sepalName = df['Name']
sepalMarks1 = df['Marks1']
sepalMarks2 = df['Marks2']
#x = con.cursor()
#x.execute("ALTER TABLE Marksheet add TotalMarks int")
# print df
df['TotalMarks']=df.apply(lambda x:x['Marks1']+x['Marks2'],axis=1)
#df.to_sql(name='Marksheet', con=con, if_exists = 'append', index=False,flavor='sqlite')
#df.to_sql(name = 'Marksheet', con = con, flavor=None, schema=None, if_exists='fail', index=True, index_label=None, chunksize=None, dtype=None)
engine = create_engine('mysql+mysqlconnector://root:Ganta@518@127.0.0.1/mydb?charset=utf8')
df.to_sql(name='Marksheet',con=engine, if_exists= 'append',index=False) '''