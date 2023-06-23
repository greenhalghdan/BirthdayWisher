import smtplib

# my_email = "**********@*****.**.**"
# password = "8888888888888888888888888"
# connection = smtplib.SMTP("eu-smtp-outbound-1.mimecast.com", 587)
# connection.starttls()
# connection.login(user=my_email, password=password)
# connection.sendmail(from_addr=my_email, to_addrs="danielgreenhalgh@suffolkmotorcyclespares.co.uk",
#                     msg="subject:hello\n\nHellothis is the body")
# connection.close()


my_email = "**********@*****.**.**"
password = "**************************"
with smtplib.SMTP("eu-smtp-outbound-1.mimecast.com", 587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs="email@recipientdomain.tld",
                        msg="subject:hello2\n\nHello this is the body")
