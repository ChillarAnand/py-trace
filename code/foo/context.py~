#import ptb; ptb.enable(context=5)

import smtplib


fromaddr = 'fromuser@gmail.com'
toaddrs  = 'touser@gmail.com'
msg = 'There was a terrible error that occured and I wanted you to know!'


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    username = 'ChillarAnand'
    password = 'HolyCow!'
    server.login(username, password)
    server.sendmail(fromaddr, toaddrs, msg)
    server.quit()


send_mail()
