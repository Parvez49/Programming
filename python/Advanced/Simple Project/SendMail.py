

import smtplib
my_email="parvezhossen81@gmail.com"
password="PH49@asdfghjkl;'"
connection=smtplib.SMTP("smtp.gmail.com",587)
connection.starttls()
connection.login(user=my_email,password=password)
connection.sendmail(from_addr=my_email,to_addrs="parvezhossen81@gmail.com",msg="hello from python")
connection.close()