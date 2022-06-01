from struct import pack
from act_process_data.connect import Connect_SQLServer

class Data_TAU(Connect_SQLServer):

    def GET_TAU(self, params):
        if params[0] == 'doanh_thu':
            cols = ['Cửa hàng', 'Tổng doanh thu']
        elif params[0] == 'chitiet_ban':
            cols = ['Mã đơn hàng','Thời gian','Loại hàng','Tên hàng','Đơn giá','Đơn vị','Số lượng','Doanh thu','Giá gốc','Chi phí','Lợi nhuận','Cửa hàng']
        elif params[0] == 'authorized':
            cols = ['ID User', 'First name', 'Last name', 'Action permission']
        params = self.convert_params(params)
        proc_name = 'exec proc_all {0}, {1}, {2}, {3}, {4}'.format(*params)
        print('[Proc] --> ' + proc_name)
        cursor = self.Call_Procedure(proc_name)
        print('-'*10)
        return self.Convert_DataFrame(cursor, cols)
        # return cursor
    
    def SALARY(self, params, insert_demo = False, check_otp = False, insert_demo_zalo=False):
        params = self.convert_params(params)
        if insert_demo == True:
            import random
            from datetime import date
            proc_name = """insert into dsa_hieu_salary 
            values ('1','4857932260991004',5,N'Trần Đình Hiếu','01.01.00.00',N'Chủ tịch',{0},{1},{2},{3},{4})
            """.format(random.randrange(100000000, 1000000000),random.randrange(100000000, 1000000000),random.randrange(100000000, 1000000000), date.today().year, date.today().month)
            print(proc_name)
            return self.Call_Procedure(proc_name, check_insert = True)
        #-> Check data to finding OTN was sign up yet
        if check_otp == True:
            proc_name = 'select * from list_salary_OTN where send_id = {0} and year(date_mfg) = year(getdate()) and MONTH(date_mfg) = month(getdate()) and date_exec is null'.format(*params)
            return self.RowCount_Data(self.Call_Procedure(proc_name))

        if insert_demo_zalo == True:
            proc_name = 'exec proc_create_user_at_fb {0}'.format(*params)
            proc_name = "EXEC proc_chatbot_create_luong_cang {0}, 'done'"
            try:
                return self.Call_Procedure(proc_name, check_insert = True)
            except:
                return 1
            
        #-> Rowcount data to set condition insert
        proc_name = 'select * from list_salary_OTN where send_id = {0} and year(date_mfg) = year(getdate()) and MONTH(date_mfg) = month(getdate()) and date_exec is null'.format(*params)
        row_num = self.RowCount_Data(self.Call_Procedure(proc_name))
        if row_num > 0:
            return 0
        #-> Procedure to insert Data of OTN
        proc_name = 'exec dsa_proc_salary_send {0}, {1}'.format(*params)
        print('[Proc] --> ' + proc_name)
        print('-'*10)
        return self.Call_Procedure(proc_name, check_insert = True)

        

