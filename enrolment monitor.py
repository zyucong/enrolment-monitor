import requests
from bs4 import BeautifulSoup
import time
import smtplib

# id can be found in the dom of the timetable page
# in the form of <a href='#S2-5479'>...</a> for COMP9032
#cid = '#S2-5479' # COMP9032
cid = '#S2-2644' # COMP9024
has_sent = False
status = 'Full'

while True:
    if has_sent:
        break
    url = 'http://timetable.unsw.edu.au/2018/COMP****.html'
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'lxml')
    data = soup.select('td a')
    for item in data:
        try:
            if item['href'] == cid:
                status_dom = item.find_next('font')
                # status is either 'Open' or 'Full'
                status = status_dom.string
                #print(status)
                break
        except:
            continue
    # send the email only once
    if status == 'Open' and not has_sent:
        # qq mail is less secure, easy to send email
        server = smtplib.SMTP_SSL('smtp.qq.com', 465)
        server.login("YOUR EMAIL ADDRESS", "YOUR TOKEN")
        msg = 'Subject: COMP**** now available!'
        # set the 'from' address,
        fromaddr = 'SENDER ADDRESS'
        # set the 'to' addresses,
        toaddr = 'RECEIVER ADDRESS'
        server.sendmail(fromaddr, toaddr, msg)
        server.quit()
        has_sent = True
        break
    # check the status every 10 minutes, allowed by robots.txt
    # Don't change it if you don't want to be banned
    time.sleep(600)

