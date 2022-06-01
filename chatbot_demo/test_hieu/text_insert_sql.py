#%%
host = 'localhost'
port = '2022'
server_name = "DESKTOP-9ES2I9R"
db_name = "test_chatbot"
uid = "sa"
pwd = "hieuvippro123"

import pymssql  
import pandas as pd
conn = pymssql.connect(host=host, port=port, server=server_name, user=uid, password=pwd, database=db_name)
        
cursor = conn.cursor()  
cursor.execute("select stt from list_salary_OTN Where token_otn = '225027322260360546611111'")  
cursor.fetchall()
print(cursor.rowcount)
conn.close()
# %%
