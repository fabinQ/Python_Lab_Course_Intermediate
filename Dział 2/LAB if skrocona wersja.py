price = 123
bonus = 23
bonus_granted = False

price = price - bonus if bonus_granted else price
print(price)
###############
rating = 4
print('very good') if rating == 5 else print('good') if rating == 4 else print('weak')
############

import datetime as dt
today_weekday = dt.date.today().strftime("%A")
print(today_weekday)
print("Pomagam mamie" if today_weekday == "Monday" else "Robisz pranie" if today_weekday == 'Tuesday' or 'Wednesday' else"Dyżur" if today_weekday == "Thusday"
      else "Na lekcje ganiasz!" if today_weekday == "Saturday" else "Niedziela jest dla nas!")