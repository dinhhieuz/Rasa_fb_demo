from underthesea import word_tokenize
from config import config as cf
from process_data.connect_tau import Data_TAU
from process_data.database import DB_TAU
from datetime import date
import datetime
import re as regex
import dateutil.relativedelta


text = "Doanh thu từ 21/0332021 đến 21/05/2021 của cửa hàng CH1 và CH2 là bao nhiêu?".lower().replace('?','')
# text = "Tôi tên là Trần Đình Hiếu"

cuahang = ['ch1','ch2','ch3']
# text_split = word_tokenize(text)
# print(text_split)

# for item in text_split:
#     if item in cf.time.keys():
#         print(cf.time[item])


text_result = 'Rất tiết chúng tôi không tìm thấy, hãy thử lại!!'

#-- Tìm ngày cụ thể

def dthu_get_param (text_result):
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
            
req, original_time, error = dthu_get_param(text)

for item in req[2]:
    item = None if item == '~' else item

print(req)
    # df = DB_TAU.GET_TAU(('doanh_thu', req[0], req[1], req[2]))

    # if df["sum_dthu"][0] != None:
    #     if req[2] is not None:
    #         num = int(df["sum_dthu"][0])
    #         text_result = f'Doanh thu là: {num:,}'

    # print(text_result)


