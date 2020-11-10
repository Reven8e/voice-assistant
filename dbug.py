from datetime import datetime

day_ = datetime.now()
day = day_.strftime("%A")
time = datetime.now()
time_h = time.strftime("%H")
time_m = time.strftime("%M")

print(day, time_h, time_m)