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

