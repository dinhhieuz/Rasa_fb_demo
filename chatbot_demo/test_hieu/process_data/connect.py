import pymssql
import pandas as pd

from datetime import datetime as dt

class Connect_SQLServer:
    # buột chạy khi hàm bị gọi
    def __init__(self, host, port, server, database, uid, pw):
        # truyền biến vào hàm __init__ chính
        self.host = host
        self.port = port
        self.server = server
        self.uid = uid
        self.pw = pw
        self.database = database
    def Convert_DataFrame(self, cursor, cols):
        '''Chuyển đổi dữ liệu lấy được về dạng DataFrame'''
        
        results = cursor.fetchall()
        df = pd.DataFrame.from_records(results, columns=cols)
        return df

    def Call_Procedure(self, proc):
        '''Kết nối đến CSDL và thực thi Procedure'''
        # Connect SQL + Python
        conn = pymssql.connect(host=self.host, port=self.port, server=self.server, user=self.uid, password=self.pw, database=self.database)
        # Tạo cursor bởi connect
        cursor = conn.cursor()
        # Thực hiện chạy proc dựa trên cursor
        cursor.execute(proc)
        return cursor


    def convert_params(self, params):
        r = []
        for val in params:
            r.append('NULL') if val is None else r.append("N'"+val+"'")
        return r