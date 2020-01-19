#!/usr/bin/env python3

import datetime
import calendar

def get_past_10_years_index_update_date(now = datetime.datetime.now()):
    calendar_init = calendar.Calendar(firstweekday = calendar.SUNDAY)
    now_date = now.date()
    now_year = now.year

    update_date = []

    for year in range(now_year - 10, now_year):
        for update_month in [6, 12]:
            index_update_date = get_third_monday(year, update_month)
            if index_update_date < now_date:
                update_date.append(index_update_date)

    return update_date

def get_third_monday(year = datetime.datetime.now().year, \
month = datetime.datetime.now().month):
    calendar_init = calendar.Calendar(firstweekday = calendar.SUNDAY)
    monthcal = calendar_init.monthdatescalendar(year, month)

    third_monday = [day for week in monthcal for day in week if \
    day.weekday() == calendar.MONDAY and \
    day.month == month][2]
    return third_monday

