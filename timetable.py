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
    url = 'http://timetable.unsw.edu.au/2019/COMP[0-9]{4}.html'
    while True:
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'lxml')
        # data = soup.findAll("td a", {"href": cid})
        data = soup.select('td a')
        status = 'Full'
        for item in data:
            if item.get("href") == cid and item.getText() == section:
                font = item.find_next('font')
                status = font.getText()
                break
        print(status, datetime.now())
        if status != 'Full':
            send_email()
            break
        time.sleep(1800)

if __name__ == '__main__':
    # id can be found in the dom of the timetable page
    # in the form of <a href='#S2-5479'>...</a> for COMP9032
    #cid = '#S2-5479' # COMP9032
    cid = 'YOUR_CID'
    section = 'CR01'
    status = 'Full'
    begin_monitor()

