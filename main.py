from datetime import date, datetime,timedelta


start_date = date.today()
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

def get_period(start_date, num_days):
    result = {}
    for i in range(num_days):
        result[(start_date.day, start_date.month)] = start_date.year
        start_date += timedelta(1)
    return result

def get_birthdays_per_week(users):
    users_dict = {day: [] for day in days}
    
    start_date = date.today()
    period = get_period(start_date, 7)
    
    for user in users:
        user_name = user["name"]
        birthday = user["birthday"]
        date_birthday = (birthday.day, birthday.month)
        
        if date_birthday in period:
            day_of_week = birthday.weekday()
            if day_of_week == 5 or day_of_week == 6:
                day_of_week = 0
            day_name = days[day_of_week]
            users_dict[day_name].append(user_name)
    
    return users_dict


if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(2023, 9, 30 ).date()},
    ]

    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
