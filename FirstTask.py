from datetime import datetime

def get_days_from_today(date):
    date_obj = datetime.strptime(date, '%Y-%m-%d').date()

    today = datetime.today().date()

    delta = today - date_obj
    return delta.days

print(f"Скільки днів пройшло: {get_days_from_today("2021-10-09")}")