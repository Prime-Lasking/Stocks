import random
import time
active = True
Stock = 100
Minutes= 0
while active:
    hours = Minutes // 60
    remaining_minutes = Minutes % 60
    days = hours // 24
    remaining_hours = hours % 24
    months = days // 30.44
    remaining_days = days % 30.44
    years = months // 12
    remaining_months = months % 12
    x: float = (random.random())
    if Stock >= 1000000:
        print("You're Rich!")
        active = False
        print(f'It took {years} years {remaining_months} months {round(remaining_days)} days {remaining_hours} hours {remaining_minutes} minutes to be a Millionaire')
        break
    if round(Stock, 2) < 0.01:
        print("You're Bankrupt!")
        active = False
        print(f'It took {years} years {remaining_months} months {round(remaining_days)} days {remaining_hours} hours {remaining_minutes} minutes to be bankrupt')
        break
    elif x <= 0.5:
            Stock = Stock+(Stock * 0.0101)
            Minutes = Minutes+1
            time.sleep(0)
            print(round(Stock, 2))
    else:
            Stock = Stock-(Stock * 0.01)
            Minutes = Minutes+1
            time.sleep(0)
            print(round(Stock, 2))


