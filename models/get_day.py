from datetime import datetime


def get_day_aliya():
    day_number = datetime.today().isoweekday() + 1
    day_aliya = "aliya" + str(day_number)
    print(day_aliya)
    print(day_number)
    return day_aliya

def get_day_name():
    day_name = datetime.today().strftime('%A')
    print(day_name)
    return day_name