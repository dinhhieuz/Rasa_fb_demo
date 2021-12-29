from datetime import date
import dateutil.relativedelta
now = date.today()
this_week = [now + dateutil.relativedelta.relativedelta(days= - now.weekday()), now]
last_week = [now + dateutil.relativedelta.relativedelta(days= - now.weekday(), weeks=-1), now + dateutil.relativedelta.relativedelta(days= - now.weekday())]

time = {
    'tuần này': f'{this_week[0]}/{this_week[1]}',
    'tuần nay': f'{this_week[0]}/{this_week[1]}',
    'tuần hôm nay': f'{this_week[0]}/{this_week[1]}',
    'thứ 2 tuần này': 'this_week',
    'thứ hai tuần này': 'this_week',
    'thứ 3 tuần này': 'this_week',
    'thứ ba tuần này': 'this_week',
    'thứ 4 tuần này': 'this_week',
    'thứ tư tuần này': 'this_week',
    'thứ 5 tuần này': 'this_week',
    'thứ năm tuần này': 'this_week',
    'thứ 6 tuần này': 'this_week',
    'thứ sau tuần này': 'this_week',
    
    'tuần trước' : f'{last_week[0]}/{last_week[1]}',
    'tuần vừa rồi': f'{last_week[0]}/{last_week[1]}',
}