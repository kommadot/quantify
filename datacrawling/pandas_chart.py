import pandas as pd
from sqlalchemy import create_engine
import pymysql
from pandas import DataFrame
from matplotlib import pyplot


pymysql.install_as_MySQLdb()
import MySQLdb

# engine = create_engine("mysql+mysqldb://root:"+"ssafy"+"@localhost/db_name", encoding='utf-8')
engine = create_engine("mysql+mysqldb://root:"+"ssafy"+"@localhost/study_db", encoding='utf-8')
conn = engine.connect()

df1 = DataFrame([
        {"deptno": 300, "dname": "학과1", "loc": "위치1"},
        {"deptno": 301, "dname": "학과2", "loc": "위치2"},
        {"deptno": 302, "dname": "학과3", "loc": "위치3"}
    ])
df1


# df.to_sql(name=table, con=engine, if_exists='append')
df1.to_sql(name="department_py", con=conn, if_exists='replace', index=True)

# 인덱스 없이 저장
# df1.to_sql(name="department_py", con=conn, if_exists='replace', index=False)
