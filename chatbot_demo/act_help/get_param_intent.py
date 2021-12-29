from act_help import config as cf
# from handle.process_data.connect_tau import Data_TAU
from act_process_data.database import DB_TAU
from act_process_data.connect_tau import Data_TAU
from datetime import date
import datetime

class Seek_param_intent():
    def intent_Dthu(text_result):
        cuahang = ['ch1','ch2','ch3']
        req = [None, None, None]
        time, original_time = None, None
        error = None
        for item_time in cf.time.keys():
            if text_result.find(item_time) != -1:
                time, original_time = cf.time[item_time].split('/'), item_time
                req[0] = time[0]
                req[1] = time[1]

        if req[0] is None and req[1] is None:
            i = 0
            for item_time in text_result.split(' '):
                if item_time.find('/') != -1 and len(item_time) == 10 :
                    try:
                        date =  item_time.split('/')
                        if len(date) == 3:
                            convert_date = datetime.datetime(int(date[2]), int(date[1]), int(date[0]))
                            req[i] = "{:%Y-%m-%d}".format(convert_date)
                            i += 1
                            if i == 2:
                                break
                        else:
                            error = 'Ngày không chính xác, vui lòng nhập đủ theo ngày/tháng/năm !'
                    except: 
                        error = 'Ngày không chính xác, vui lòng nhập đủ theo ngày/tháng/năm !'
        
        list_store = []
        for item_store in text_result.split(' '):
            if item_store in cuahang:
                list_store.append(item_store)
            
        req[2] = list_store if len(list_store) > 0 else '~' 

        return req, original_time, error
        
    ''' Chuyển đổi kiểu show cho khách hàng sang dạng Date SQL '''
    def convert_date_show_to_sql(date):
        date = date.split('/')
        convert_date = datetime.datetime(int(date[2]), int(date[1]), int(date[0]))
        result = "{:%Y-%m-%d}".format(convert_date)
        return result
    ''' Chuyển đổi kiểu dạng SQL sang kiểu show cho khách hàng '''
    def convert_date_sql_to_show(date):
        date = date.split('-')
        convert_date = datetime.datetime(int(date[0]), int(date[1]), int(date[2]))
        result = "{:%d/%m/%Y}".format(convert_date)
        return result
