from datetime import date
import dateutil.relativedelta
import gc
now = date.today()

this_week = [now + dateutil.relativedelta.relativedelta(days= - now.weekday()), now]
this_week_2 = now + dateutil.relativedelta.relativedelta(days= - now.weekday())
this_week_3 = now + dateutil.relativedelta.relativedelta(days= - now.weekday() + 1)
this_week_4 = now + dateutil.relativedelta.relativedelta(days= - now.weekday() + 2)
this_week_5 = now + dateutil.relativedelta.relativedelta(days= - now.weekday() + 3)
this_week_6 = now + dateutil.relativedelta.relativedelta(days= - now.weekday() + 4)
this_week_7 = now + dateutil.relativedelta.relativedelta(days= - now.weekday() + 5)
this_week_cn = now + dateutil.relativedelta.relativedelta(days= - now.weekday() + 6)

last_week = [now + dateutil.relativedelta.relativedelta(days= - now.weekday(), weeks=-1), now + dateutil.relativedelta.relativedelta(days= - now.weekday())]
last_week_2 = now + dateutil.relativedelta.relativedelta(days= - now.weekday(), weeks=-1)
last_week_3 = now + dateutil.relativedelta.relativedelta(days= - now.weekday() + 1, weeks=-1)
last_week_4 = now + dateutil.relativedelta.relativedelta(days= - now.weekday() + 2, weeks=-1)
last_week_5 = now + dateutil.relativedelta.relativedelta(days= - now.weekday() + 3, weeks=-1)
last_week_6 = now + dateutil.relativedelta.relativedelta(days= - now.weekday() + 4, weeks=-1)
last_week_7 = now + dateutil.relativedelta.relativedelta(days= - now.weekday() + 5, weeks=-1)
last_week_cn = now + dateutil.relativedelta.relativedelta(days= - now.weekday() + 6, weeks=-1)

start_this_month = date(now.year,now.month,1)
this_month = [start_this_month, start_this_month + dateutil.relativedelta.relativedelta(months = 1, days= -1)]
last_month = [start_this_month + dateutil.relativedelta.relativedelta(months = -1), start_this_month + dateutil.relativedelta.relativedelta(months = 0, days= -1)]

start_this_year = date(now.year,1,1)
this_year = [start_this_year, start_this_year + dateutil.relativedelta.relativedelta(years = 1, days= -1)]
last_year = [start_this_year + dateutil.relativedelta.relativedelta(years = -1), start_this_year + dateutil.relativedelta.relativedelta(years = 0, days= -1)]


time = {

    'hôm nay': f'{now}/{now}',
    'ngày ni': f'{now}/{now}',
    'bửa ni': f'{now}/{now}',

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

    'tuần này': f'{this_week[0]}/{this_week[1]}',
    'tuần nay': f'{this_week[0]}/{this_week[1]}',
    'tuần hôm nay': f'{this_week[0]}/{this_week[1]}',
    'tuần trước' : f'{last_week[0]}/{last_week[1]}',
    'tuần vừa rồi': f'{last_week[0]}/{last_week[1]}',

    'tháng này': f'{this_month[0]}/{this_month[1]}',
    'tháng ni': f'{this_month[0]}/{this_month[1]}',
    'tháng trước': f'{last_month[0]}/{last_month[1]}',

    'năm nay': f'{this_year[0]}/{this_year[1]}',
    'năm ni': f'{this_year[0]}/{this_year[1]}',
    'năm này': f'{this_year[0]}/{this_year[1]}',
    'năm trước': f'{last_year[0]}/{last_year[1]}',
    'năm vừa rồi': f'{last_year[0]}/{last_year[1]}',

}
#--- Clear value

# del now, time
# del this_week,this_week_2,this_week_3,this_week_4,this_week_5,this_week_6,this_week_7,this_week_cn
# del last_week,last_week_2,last_week_3,last_week_4
# del last_week_5,last_week_6,last_week_7,last_week_cn
# del start_this_month,this_month,last_month
# del start_this_year,this_year,last_year

# gc.collect()