from datetime import datetime, timedelta

today = datetime.now()

print(today)

first_of_the_year = datetime(2022, 1, 1)
how_many_days = today - first_of_the_year
day_increment = timedelta(days=1)
tomorrow = today + day_increment
print(how_many_days)
print(tomorrow)