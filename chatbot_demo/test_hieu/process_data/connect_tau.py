from process_data.connect import Connect_SQLServer

class Data_TAU(Connect_SQLServer):

    def GET_TAU(self, params):
        if params[0] == 'doanh_thu':
            cols = ['sum_dthu']

        params = self.convert_params(params)
        proc_name = 'exec proc_all {0}, {1}, {2}, {3}'.format(*params)
        print(proc_name)
        cursor = self.Call_Procedure(proc_name)

        return self.Convert_DataFrame(cursor, cols)
        # return cursor

