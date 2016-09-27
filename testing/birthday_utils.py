import datetime

def get_today():
    return datetime.date.today()

def get_age(birthdate):
    today = get_today()
    age = today.year - birthdate.year

    # birthday_this_year = birthdate.replace(year=birthdate.year + age)
    # if today < birthday_this_year:
    #     age -= 1

    if (today.month, today.day) < (birthdate.month, birthdate.day):
        age -= 1
    return age
