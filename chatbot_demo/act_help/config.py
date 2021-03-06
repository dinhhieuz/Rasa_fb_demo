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
    'h??m nay': f'{now}/{now}',
    'ng??y ni': f'{now}/{now}',
    'b???a ni': f'{now}/{now}',
    
    'h??m qua': f'{yesterday}/{yesterday}',
    'h??m v???a r???i': f'{yesterday}/{yesterday}',

    'th??? 2 tu???n n??y': f'{this_week_2}/{this_week_2}',
    'th??? hai tu???n n??y': f'{this_week_2}/{this_week_2}',
    'th??? 3 tu???n n??y': f'{this_week_3}/{this_week_3}',
    'th??? ba tu???n n??y': f'{this_week_3}/{this_week_3}',
    'th??? 4 tu???n n??y': f'{this_week_4}/{this_week_4}',
    'th??? t?? tu???n n??y': f'{this_week_4}/{this_week_4}',
    'th??? 5 tu???n n??y': f'{this_week_5}/{this_week_5}',
    'th??? n??m tu???n n??y': f'{this_week_5}/{this_week_5}',
    'th??? 6 tu???n n??y': f'{this_week_6}/{this_week_6}',
    'th??? sau tu???n n??y': f'{this_week_6}/{this_week_6}',
    'th??? 7 tu???n n??y': f'{this_week_7}/{this_week_7}',
    'th??? b???y tu???n n??y': f'{this_week_7}/{this_week_7}',
    'ch??? nh???t tu???n n??y': f'{this_week_cn}/{this_week_cn}',
    'cn tu???n n??y': f'{this_week_cn}/{this_week_cn}',

    'th??? 2 tu???n tr?????c': f'{last_week_2}/{last_week_2}',
    'th??? hai tu???n tr?????c': f'{last_week_2}/{last_week_2}',
    'th??? 3 tu???n tr?????c': f'{last_week_3}/{last_week_3}',
    'th??? ba tu???n tr?????c': f'{last_week_3}/{last_week_3}',
    'th??? 4 tu???n tr?????c': f'{last_week_4}/{last_week_4}',
    'th??? t?? tu???n tr?????c': f'{last_week_4}/{last_week_4}',
    'th??? 5 tu???n tr?????c': f'{last_week_5}/{last_week_5}',
    'th??? n??m tu???n tr?????c': f'{last_week_5}/{last_week_5}',
    'th??? 6 tu???n tr?????c': f'{last_week_6}/{last_week_6}',
    'th??? sau tu???n tr?????c': f'{last_week_6}/{last_week_6}',
    'th??? 7 tu???n tr?????c': f'{last_week_7}/{last_week_7}',
    'th??? b???y tu???n tr?????c': f'{last_week_7}/{last_week_7}',
    'ch??? nh???t tu???n tr?????c': f'{last_week_cn}/{last_week_cn}',
    'cn tu???n tr?????c': f'{last_week_cn}/{last_week_cn}',

    'th??? 2 tu???n v???a r???i': f'{last_week_2}/{last_week_2}',
    'th??? hai tu???n v???a r???i': f'{last_week_2}/{last_week_2}',
    'th??? 3 tu???n v???a r???i': f'{last_week_3}/{last_week_3}',
    'th??? ba tu???n v???a r???i': f'{last_week_3}/{last_week_3}',
    'th??? 4 tu???n v???a r???i': f'{last_week_4}/{last_week_4}',
    'th??? t?? tu???n v???a r???i': f'{last_week_4}/{last_week_4}',
    'th??? 5 tu???n v???a r???i': f'{last_week_5}/{last_week_5}',
    'th??? n??m tu???n v???a r???i': f'{last_week_5}/{last_week_5}',
    'th??? 6 tu???n v???a r???i': f'{last_week_6}/{last_week_6}',
    'th??? sau tu???n v???a r???i': f'{last_week_6}/{last_week_6}',
    'th??? 7 tu???n v???a r???i': f'{last_week_7}/{last_week_7}',
    'th??? b???y tu???n v???a r???i': f'{last_week_7}/{last_week_7}',
    'ch??? nh???t tu???n v???a r???i': f'{last_week_cn}/{last_week_cn}',
    'cn tu???n v???a r???i': f'{last_week_cn}/{last_week_cn}',

    'tu???n n??y': f'{this_week[0]}/{this_week[1]}',
    'tu???n nay': f'{this_week[0]}/{this_week[1]}',
    'tu???n h??m nay': f'{this_week[0]}/{this_week[1]}',
    'tu???n tr?????c' : f'{last_week[0]}/{last_week[1]}',
    'tu???n v???a r???i': f'{last_week[0]}/{last_week[1]}',

    'th??ng n??y': f'{this_month[0]}/{this_month[1]}',
    'th??ng ni': f'{this_month[0]}/{this_month[1]}',
    'th??ng tr?????c': f'{last_month[0]}/{last_month[1]}',
    'th??ng v???a r???i': f'{last_month[0]}/{last_month[1]}',

    'qu?? 1 n??m tr?????c': f'{l_first_quarter[0]}/{l_first_quarter[1]}', 
    'qu?? m???t n??m tr?????c': f'{l_first_quarter[0]}/{l_first_quarter[1]}', 
    'qu?? 2 n??m tr?????c': f'{l_second_quarter[0]}/{l_second_quarter[1]}', 
    'qu?? hai n??m tr?????c': f'{l_second_quarter[0]}/{l_second_quarter[1]}', 
    'qu?? 3 n??m tr?????c': f'{l_third_quarter[0]}/{l_third_quarter[1]}', 
    'qu?? ba n??m tr?????c': f'{l_third_quarter[0]}/{l_third_quarter[1]}', 
    'qu?? 4 n??m tr?????c': f'{l_fourth_quarter[0]}/{l_fourth_quarter[1]}', 
    'qu?? b???n n??m tr?????c': f'{l_fourth_quarter[0]}/{l_fourth_quarter[1]}', 

    'qu?? m???t': f'{first_quarter[0]}/{first_quarter[1]}', 
    'qu?? hai': f'{second_quarter[0]}/{second_quarter[1]}', 
    'qu?? ba': f'{third_quarter[0]}/{third_quarter[1]}', 
    'qu?? b???n': f'{fourth_quarter[0]}/{fourth_quarter[1]}', 

    'n??m nay': f'{this_year[0]}/{this_year[1]}',
    'n??m ni': f'{this_year[0]}/{this_year[1]}',
    'n??m n??y': f'{this_year[0]}/{this_year[1]}',
    'n??m tr?????c': f'{last_year[0]}/{last_year[1]}',
    'n??m v???a r???i': f'{last_year[0]}/{last_year[1]}',

}