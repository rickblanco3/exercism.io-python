import calendar
import datetime

class MeetupException(Exception):
    pass

def meetup_day(yr,mo,weekday,desc):
    day_of_month = 0
    cal = calendar.monthcalendar(yr,mo)
    wkday_attr = getattr(calendar,weekday.upper())
    wkdays = [wk[wkday_attr] for wk in cal if wk[wkday_attr] != 0]
    
    try:
        if desc == '1st':
            day_of_month = wkdays[0]
        elif desc == '2nd':
            day_of_month = wkdays[1]
        elif desc == '3rd':
            day_of_month = wkdays[2]
        elif desc == '4th':
            day_of_month = wkdays[3]
        elif desc == '5th':
            day_of_month = wkdays[4]
        elif desc == 'teenth':
            i = iter(wkdays)
            day_of_month = i.next()
            while day_of_month not in range(13,20):
                day_of_month = i.next()
        elif desc == 'last':
            day_of_month = wkdays[-1]
    except:
        raise MeetupException()
    
    return datetime.date(yr,mo,day_of_month)
