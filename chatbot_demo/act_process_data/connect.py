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

    def RowCount_Data(self, cursor):
        '''Đếm số dòng kết quả bảng''' 
        cursor.fetchall()
        return cursor.rowcount

    def Call_Procedure(self, proc, check_insert=False):
        '''Kết nối đến CSDL và thực thi Procedure'''
        # Connect SQL + Python        
        conn = pymssql.connect(host=self.host, port=self.port, server=self.server, user=self.uid, password=self.pw, database=self.database)
        # Tạo cursor bởi connect
        cursor = conn.cursor()
        # Thực hiện chạy proc dựa trên cursor
        cursor.execute(proc)
        # Nếu dùng để update data thì commit
        if check_insert == True:
            conn.commit()
            return cursor.rowcount
        # cursor.close()
        # conn.close()
        return cursor


    def convert_params(self, params):
        r = []
        
        if type(params) == tuple:
            for val in params:
                r.append('NULL') if val is None else r.append("N'"+val+"'")
        if type(params) == str:
            r.append("N'"+params+"'")

        return r