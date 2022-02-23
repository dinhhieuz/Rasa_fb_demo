from datetime import date, datetime
from distutils.log import error
import gc
t = 'xem doanh thu ngày 12 tháng 5 năm 2021 đến nay'.split(' ')
try:
    #lấy ngày hiện tại để làm mặc định
    now = datetime.today()
    l = {
        'ngày' : 1,
        'tháng': now.month,
        'năm' : now.year
    }
    # tìm có chữ ngày/tháng/năm hay k, nếu có thì lấy ô trước kí tự tìm đc 1 đơn vị
    for i in range(len(t)):
        if t[i] == 'ngày' and int(t[i+1]): l['ngày'] = t[i+1]
        if t[i] == 'tháng' and int(t[i+1]): l['tháng'] = t[i+1]
        if t[i] == 'năm' and int(t[i+1]): l['năm'] = t[i+1]
    begin = ('{2}-{1}-{0}'.format(l['ngày'],l['tháng'], l['năm']))
    # Hợp mãng để tìm xem có 'đến nay' or 'bay giờ' không
    mrg_text = ' '.join(t)
    if mrg_text.find('đến nay') != -1 or mrg_text.find('bây giờ') != -1:
        end = '{:%Y-%m-%d}'.format(datetime.today())
    else:
        end = begin
except Exception as error:
    print('Vui lòng nhập rõ ngày tháng năm !!!')

print(begin,'  ',end)



