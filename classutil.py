import requests
from bs4 import BeautifulSoup
import time
import smtplib
from datetime import datetime

def send_email():
    s = smtplib.SMTP('YOUR_SMTP_SERVER')
    s.connect('YOUR_SMTP_SERVER', YOUR_PORT_NUMBER)
    s.starttls()
    s.login('AWS_SMTP_USERNMAE', 'AWS_SMTP_CREDENTIAL')
    msg = 'From: email@example.com\nTo: email@example.com\nSubject: COMP**** now available (Found in timetable)'
    # set the 'from' address,
    fromaddr = 'email@example.com'
    # set the 'to' addresses,
    toaddr = 'email@example.com'
    # s.sendmail(fromaddr, toaddr, msg)
    try:
        s.sendmail(fromaddr, toaddr, msg)
    finally:
        s.quit()


def begin_monitor():
    url = 'http://classutil.unsw.edu.au/COMP_T2.html'
    while True:
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'lxml')
        # data = soup.findAll("td a", {"href": cid})
        data = soup.select('td')
        status = 'Full'
        for item in data:
            # print(item.getText())
            if item.getText().strip() == cla:
                neigobour = item.findNext().findNext()
                status = neigobour.getText()
                break
        print(status, datetime.now())
        if status != 'Full':
            print("got it")
            send_email()
            break
        time.sleep(1800)

if __name__ == '__main__':
    # id can be found in the DOM of the classutil page
    # cla = '2235'  # COMP9315
    status = 'Full'
    begin_monitor()

