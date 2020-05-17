#https://realpython.com/python-datetime/




if __name__ == "__main__":
    import time
    print(time.time())



    #datetime provides three classes that make up the high-level interface that most people will use:  datetime.date is an idealized date that assumes the Gregorian calendar extends infinitely into the future and past.     This object stores the year, month, and day as attributes. datetime.time is an idealized time that assumes there are 86,400 seconds per day with no leap seconds. This object stores the hour, minute, second, microsecond, and tzinfo (time zone information).datetime.datetime is a combination of a date and a time. It has all the attributes of both classes.


    from datetime import date, time, datetime

    print(date(year=2020, month=1, day=31))

    print(time(hour=13, minute=14, second=31))

    print(datetime(year=2020, month=1, day=31, hour=13, minute=14, second=31))


    #easier methods are

    today = date.today();
    print(today)

    now = datetime.now();
    print(now)

    current_time = time(now.hour, now.minute, now.second)
    print(current_time)

    print(datetime.combine(today, current_time))


    #Using Strings to Create Python datetime Instances

    #if in iso format

    from datetime import date
    print(date.fromisoformat("2020-01-31"))


    #But what if you have a string that represents a date and time but isnt in the ISO 8601 format?
    
    
    date_string = "01-31-2020 14:45:37"
    format_string = "%m-%d-%Y %H:%M:%S"

    from datetime import datetime

    print(datetime.strptime(date_string, format_string))

    #import dateparser


    #Working With Time Zones

    #Using dateutil to Add Time Zones to Python datetime. One reason that dateutil is so useful is that it includes an interface to the IANA time zone database. This takes the hassle out of assigning time zones to your datetime instances.


    from dateutil import tz
    now = datetime.now(tz = tz.tzlocal())
    print(now)

    print(now.tzname())


    #passing particular timezone

    London_tz = tz.gettz("Europe/London")
    now = datetime.now(tz=London_tz)
    print(now)

    print(now.tzname())

    #passing UTC

    print(datetime.now(tz=tz.UTC))


    #Doing Arithmetic With Python datetime

    from datetime import datetime, timedelta

    now = datetime.now()

    print(now)

    tomorrow = timedelta(days=+1)
    print(now+tomorrow)

    yesterday = timedelta(days=-1)
    print(now+yesterday)

    delta = timedelta(days=+3, hours=-4)
    print(now + delta)

    #timedelta is very useful in this way, but its somewhat limited because it cannot add or subtract intervals larger than a day, such as a month or a year. Fortunately, dateutil provides a more powerful replacement called relativedelta.


    from dateutil.relativedelta import relativedelta
    tomorrow = relativedelta(days=+1)
    print(now + tomorrow)


    delta = relativedelta(years=+5, months=+1, days=+3, hours=-4, minutes=-30)
    print(now + delta)

    print(now)

    tomorrow = datetime(2020, 1, 27, 9, 37, 46, 380905)

    print(relativedelta(now, tomorrow))


