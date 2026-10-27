from datetime import datetime
now = datetime.now()
print(now)                      # 2021-07-08 07:34:46.549883
day = now.day                   # 8
month = now.month               # 7
year = now.year                 # 2021
hour = now.hour                 # 7
minute = now.minute             # 38
second = now.second
timestamp = now.timestamp()
print(day, month, year, hour, minute)
print('timestamp', timestamp)
print(f'{day}/{month}/{year}, {hour}:{minute}')  # 8/7/2021, 7:38

# date et heure actuelles
now = datetime.now()
t = now.strftime("%H:%M:%S")
print("heure :", t)           # heure : 18:21:40
time_one = now.strftime("%m/%d/%Y, %H:%M:%S")
# format mm/dd/YY H:M:S
print("heure une :", time_one)        # heure une : 06/28/2022, 18:21:40
time_two = now.strftime("%d/%m/%Y, %H:%M:%S")
# format dd/mm/YY H:M:S
print("heure deux :", time_two)        # heure deux : 28/06/2022, 18:21:40