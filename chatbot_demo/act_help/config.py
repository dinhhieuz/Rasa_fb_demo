from datetime import date
import dateutil.relativedelta
import gc
#-> Today
now = date.today()
#-> yesterday
yesterday = now + dateutil.relativedelta.relativedelta(days = -1)
#-> week
this_week = [now + dateutil.relativedelta.relativedelta(days= - now.weekday()), now]
#-> day of week
this_week_2 = now + dateutil.relativedelta.relativedelta(days= - now.weekday())
this_week_3 = now + dateutil.relativedelta.relativedelta(days= - now.weekday() + 1)
this_week_4 = now + dateutil.relativedelta.relativedelta(days= - now.weekday() + 2)
this_week_5 = now + dateutil.relativedelta.relativedelta(days= - now.weekday() + 3)
this_week_6 = now + dateutil.relativedelta.relativedelta(days= - now.weekday() + 4)
this_week_7 = now + dateutil.relativedelta.relativedelta(days= - now.weekday() + 5)
this_week_cn = now + dateutil.relativedelta.relativedelta(days= - now.weekday() + 6)
#-> day of last week
last_week = [now + dateutil.relativedelta.relativedelta(days= - now.weekday(), weeks=-1), now + dateutil.relativedelta.relativedelta(days= - now.weekday())]
#-> last week
last_week_2 = now + dateutil.relativedelta.relativedelta(days= - now.weekday(), weeks=-1)
last_week_3 = now + dateutil.relativedelta.relativedelta(days= - now.weekday() + 1, weeks=-1)
last_week_4 = now + dateutil.relativedelta.relativedelta(days= - now.weekday() + 2, weeks=-1)
last_week_5 = now + dateutil.relativedelta.relativedelta(days= - now.weekday() + 3, weeks=-1)
last_week_6 = now + dateutil.relativedelta.relativedelta(days= - now.weekday() + 4, weeks=-1)
last_week_7 = now + dateutil.relativedelta.relativedelta(days= - now.weekday() + 5, weeks=-1)
last_week_cn = now + dateutil.relativedelta.relativedelta(days= - now.weekday() + 6, weeks=-1)
#-> begining day of month
start_this_month = date(now.year,now.month,1)
#-> a month
this_month = [start_this_month, start_this_month + dateutil.relativedelta.relativedelta(months = 1, days= -1)]
#-> last month
last_month = [start_this_month + dateutil.relativedelta.relativedelta(months = -1), start_this_month + dateutil.relativedelta.relativedelta(months = 0, days= -1)]
 
#-> first day of year
start_this_year = date(now.year,1,1)
date_last_year = start_this_year + dateutil.relativedelta.relativedelta(years = -1)
#-> a year
this_year = [start_this_year, start_this_year + dateutil.relativedelta.relativedelta(years = 1, days= -1)]
#-> last year
last_year = [start_this_year + dateutil.relativedelta.relativedelta(years = -1), start_this_year + dateutil.relativedelta.relativedelta(years = 0, days= -1)]
#-> This quarter
first_quarter = [start_this_year, start_this_year + dateutil.relativedelta.relativedelta(months= 3, days= - 1)]
second_quarter = [start_this_year + dateutil.relativedelta.relativedelta(months= 3), start_this_year + dateutil.relativedelta.relativedelta(months= 3+3, days= - 1)]
third_quarter = [start_this_year + dateutil.relativedelta.relativedelta(months= 3+3), start_this_year + dateutil.relativedelta.relativedelta(months= 3+3+3, days= - 1)]
fourth_quarter = [start_this_year + dateutil.relativedelta.relativedelta(months= 3+3+3), start_this_year + dateutil.relativedelta.relativedelta(months= 3+3+3+3, days= - 1)]

l_first_quarter = [date_last_year, date_last_year + dateutil.relativedelta.relativedelta(months= 3, days= - 1)]
l_second_quarter = [date(now.year-1,4,1), date_last_year + dateutil.relativedelta.relativedelta(months= 3+3, days= - 1)]
l_third_quarter = [date(now.year-1,7,1), date_last_year + dateutil.relativedelta.relativedelta(months= 3+3+3, days= - 1)]
l_fourth_quarter = [date(now.year-1,10,1), date_last_year + dateutil.relativedelta.relativedelta(months= 3+3+3+3, days= - 1)]


time = {
    'hôm nay': f'{now}/{now}',
    'ngày ni': f'{now}/{now}',
    'bửa ni': f'{now}/{now}',
    
    'hôm qua': f'{yesterday}/{yesterday}',
    'hôm vừa rồi': f'{yesterday}/{yesterday}',

    'thứ 2 tuần này': f'{this_week_2}/{this_week_2}',
    'thứ hai tuần này': f'{this_week_2}/{this_week_2}',
    'thứ 3 tuần này': f'{this_week_3}/{this_week_3}',
    'thứ ba tuần này': f'{this_week_3}/{this_week_3}',
    'thứ 4 tuần này': f'{this_week_4}/{this_week_4}',
    'thứ tư tuần này': f'{this_week_4}/{this_week_4}',
    'thứ 5 tuần này': f'{this_week_5}/{this_week_5}',
    'thứ năm tuần này': f'{this_week_5}/{this_week_5}',
    'thứ 6 tuần này': f'{this_week_6}/{this_week_6}',
    'thứ sau tuần này': f'{this_week_6}/{this_week_6}',
    'thứ 7 tuần này': f'{this_week_7}/{this_week_7}',
    'thứ bảy tuần này': f'{this_week_7}/{this_week_7}',
    'chủ nhật tuần này': f'{this_week_cn}/{this_week_cn}',
    'cn tuần này': f'{this_week_cn}/{this_week_cn}',

    'thứ 2 tuần trước': f'{last_week_2}/{last_week_2}',
    'thứ hai tuần trước': f'{last_week_2}/{last_week_2}',
    'thứ 3 tuần trước': f'{last_week_3}/{last_week_3}',
    'thứ ba tuần trước': f'{last_week_3}/{last_week_3}',
    'thứ 4 tuần trước': f'{last_week_4}/{last_week_4}',
    'thứ tư tuần trước': f'{last_week_4}/{last_week_4}',
    'thứ 5 tuần trước': f'{last_week_5}/{last_week_5}',
    'thứ năm tuần trước': f'{last_week_5}/{last_week_5}',
    'thứ 6 tuần trước': f'{last_week_6}/{last_week_6}',
    'thứ sau tuần trước': f'{last_week_6}/{last_week_6}',
    'thứ 7 tuần trước': f'{last_week_7}/{last_week_7}',
    'thứ bảy tuần trước': f'{last_week_7}/{last_week_7}',
    'chủ nhật tuần trước': f'{last_week_cn}/{last_week_cn}',
    'cn tuần trước': f'{last_week_cn}/{last_week_cn}',

    'thứ 2 tuần vừa rồi': f'{last_week_2}/{last_week_2}',
    'thứ hai tuần vừa rồi': f'{last_week_2}/{last_week_2}',
    'thứ 3 tuần vừa rồi': f'{last_week_3}/{last_week_3}',
    'thứ ba tuần vừa rồi': f'{last_week_3}/{last_week_3}',
    'thứ 4 tuần vừa rồi': f'{last_week_4}/{last_week_4}',
    'thứ tư tuần vừa rồi': f'{last_week_4}/{last_week_4}',
    'thứ 5 tuần vừa rồi': f'{last_week_5}/{last_week_5}',
    'thứ năm tuần vừa rồi': f'{last_week_5}/{last_week_5}',
    'thứ 6 tuần vừa rồi': f'{last_week_6}/{last_week_6}',
    'thứ sau tuần vừa rồi': f'{last_week_6}/{last_week_6}',
    'thứ 7 tuần vừa rồi': f'{last_week_7}/{last_week_7}',
    'thứ bảy tuần vừa rồi': f'{last_week_7}/{last_week_7}',
    'chủ nhật tuần vừa rồi': f'{last_week_cn}/{last_week_cn}',
    'cn tuần vừa rồi': f'{last_week_cn}/{last_week_cn}',

    'tuần này': f'{this_week[0]}/{this_week[1]}',
    'tuần nay': f'{this_week[0]}/{this_week[1]}',
    'tuần hôm nay': f'{this_week[0]}/{this_week[1]}',
    'tuần trước' : f'{last_week[0]}/{last_week[1]}',
    'tuần vừa rồi': f'{last_week[0]}/{last_week[1]}',

    'tháng này': f'{this_month[0]}/{this_month[1]}',
    'tháng ni': f'{this_month[0]}/{this_month[1]}',
    'tháng trước': f'{last_month[0]}/{last_month[1]}',
    'tháng vừa rồi': f'{last_month[0]}/{last_month[1]}',

    'quý 1 năm trước': f'{l_first_quarter[0]}/{l_first_quarter[1]}', 
    'quý một năm trước': f'{l_first_quarter[0]}/{l_first_quarter[1]}', 
    'quý 2 năm trước': f'{l_second_quarter[0]}/{l_second_quarter[1]}', 
    'quý hai năm trước': f'{l_second_quarter[0]}/{l_second_quarter[1]}', 
    'quý 3 năm trước': f'{l_third_quarter[0]}/{l_third_quarter[1]}', 
    'quý ba năm trước': f'{l_third_quarter[0]}/{l_third_quarter[1]}', 
    'quý 4 năm trước': f'{l_fourth_quarter[0]}/{l_fourth_quarter[1]}', 
    'quý bốn năm trước': f'{l_fourth_quarter[0]}/{l_fourth_quarter[1]}', 

    'quý một': f'{first_quarter[0]}/{first_quarter[1]}', 
    'quý hai': f'{second_quarter[0]}/{second_quarter[1]}', 
    'quý ba': f'{third_quarter[0]}/{third_quarter[1]}', 
    'quý bốn': f'{fourth_quarter[0]}/{fourth_quarter[1]}', 

    'năm nay': f'{this_year[0]}/{this_year[1]}',
    'năm ni': f'{this_year[0]}/{this_year[1]}',
    'năm này': f'{this_year[0]}/{this_year[1]}',
    'năm trước': f'{last_year[0]}/{last_year[1]}',
    'năm vừa rồi': f'{last_year[0]}/{last_year[1]}',

}