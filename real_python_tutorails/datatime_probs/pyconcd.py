




if __name__ == "__main__":
    from datetime import datetime

    PYCON_DATE = datetime(year=2021, month=5, day=12, hour=8)
    countdate = PYCON_DATE - datetime.now()
    print(f'Countdown to pycon 2021: {countdate}')

    from dateutil import parser, tz

    PYCON_DATE = parser.parse("May 12, 2021 8:00 AM")
    PYCON_DATE = PYCON_DATE.replace(tzinfo=tz.gettz("America/New_York"))
    now = datetime.now(tz=tz.tzlocal())

    countdown = PYCON_DATE - now
    print(f"Countdown to PyCon US 2021: {countdown}")

    from dateutil.relativedelta import relativedelta


    countdown = relativedelta(PYCON_DATE, now)
    print(f"Countdown to PyCon US 2021: {countdown}")



    def time_amount(time_unit: str, countdown: relativedelta) -> str:
        t = getattr(countdown, time_unit)
        return f"{t} {time_unit}" if t != 0 else ""

    countdown = relativedelta(PYCON_DATE, now)
    time_units = ["years", "months", "days", "hours", "minutes", "seconds"]
    output = (t for tu in time_units if (t := time_amount(tu, countdown)))
    print("Countdown to PyCon US 2021:", ", ".join(output))
    
    def main():
        now = datetime.now(tz=tz.tzlocal())
        countdown = relativedelta(PYCON_DATE, now)
        time_units = ["years", "months", "days", "hours", "minutes", "seconds"]
        output = (t for tu in time_units if (t := time_amount(tu, countdown)))
        pycon_date_str = PYCON_DATE.strftime("%A, %B %d, %Y at %H:%M %p %Z")
        print(f"PyCon US 2021 will start on:", pycon_date_str)
        print("Countdown to PyCon US 2021:", ", ".join(output))

    main()
