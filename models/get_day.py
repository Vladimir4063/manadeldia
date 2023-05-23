from datetime import datetime


def get_day_number():
    day_number = datetime.today().isoweekday() + 1
    day_aliya = "aliya" + str(day_number)
    print(day_aliya)
    return day_number

def get_day_name():
    day_name = datetime.today().strftime('%A')
    print(day_name)
    return day_name