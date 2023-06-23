import smtplib
import datetime as dt
import random
# my_email = "**********@*****.**.**"
# password = "8888888888888888888888888"
# connection = smtplib.SMTP("eu-smtp-outbound-1.mimecast.com", 587)
# connection.starttls()
# connection.login(user=my_email, password=password)
# connection.sendmail(from_addr=my_email, to_addrs="danielgreenhalgh@suffolkmotorcyclespares.co.uk",
#                     msg="subject:hello\n\nHellothis is the body")
# connection.close()

#
# my_email = "**********@*****.**.**"
# password = "**************************"
# with smtplib.SMTP("eu-smtp-outbound-1.mimecast.com", 587) as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email, to_addrs="email@recipientdomain.tld",
#                         msg="subject:hello2\n\nHello this is the body")

# now = dt.datetime.now()
# year = now.year
# month = now.month
# dayofweek = now.weekday()
# print(dayofweek)
#
# date_of_birth = dt.datetime(year=1995, month=6, day=15, hour=4)
# print(date_of_birth)

#sending a motivational quote

#todo: use datetime module to obtain curretn day of week

now = dt.datetime.now()
day_of_week = now.weekday()

#todo: open quotes.txt and obtain list of quotes
with open("quotes.txt") as quotes:
    quotes = [quote for quote in quotes]

#todo: use random module to pick a random quote fro the list

random_quote = random.choice(quotes)

#todo: use SMTPlib to send email to my self
if day_of_week == 0:
    email_address = input("Please enter your email address: ")
    password = input("Please enter your password: ")
    with smtplib.SMTP("eu-smtp-outbound-1.mimecast.com", 587) as connection:
        connection.starttls()
        connection.login(user=email_address, password=password)
        connection.sendmail(from_addr=email_address, to_addrs="email@domain.tld",
                            msg=f"subject:MotivationalQuote\n\n{random_quote}")

