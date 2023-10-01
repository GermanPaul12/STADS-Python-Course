#Monday Motivation Project
import yagmail
import datetime as dt
import random

MY_EMAIL = "appbreweryinfo@gmail.com"
MY_PASSWORD = "abcd1234()"

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 1:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)
    # yagmail.register(MY_EMAIL, MY_PASSWORD)
    # yag = yagmail.SMTP(MY_EMAIL)
    yag = yagmail.SMTP("automatedbygerman@gmail.com")
    yag.send(to=["tinnier.dryer0w@icloud.com"],
             subject="Motivational Quote",
             )
