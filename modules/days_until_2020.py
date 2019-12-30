import datetime


def season_2020_start():
    start_date = datetime.datetime(2020, 1, 8)
    today_date = datetime.datetime.today()
    date_difference = start_date - today_date
    message = ''

    if today_date < start_date:
        message = 'There are {} days until "Season 2020" begins! *(January 8th!)*'.format(date_difference.days)
    elif today_date >= start_date:
        message = '"Season 2020" has already started!'

    return message