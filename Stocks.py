import random
import time
active = True
Stock = 100
Minutes= 0
history = []
input = int(input('Do you want a log scale or a normal graph type 1 if log scale type 2 for normal graph'))

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
    elif round(Stock, 2) < 0.01:
        print("You're Bankrupt!")
        active = False
        print(f'It took {years} years {remaining_months} months {round(remaining_days)} days {remaining_hours} hours {remaining_minutes} minutes to be bankrupt')
        break
    change = Stock * (0.0101 if x <= 0.5 else -0.01)
    Stock += change
    print(round(Stock,2))
    if input == 1:
        history.append(math.log10(Stock))
    else:
        history.append(Stock)
    Minutes += 1
    time.sleep(0)
plt.plot(history, label='Stock Value', color='green')
plt.title("Stock Simulation Over Time")
plt.xlabel("Minutes")
plt.ylabel("Stock Price")
plt.grid(True)
plt.legend()
plt.show()


