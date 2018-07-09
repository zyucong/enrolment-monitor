# enrolment-monitor
### Background

Some popular courses in UNSW is hard to enroll in. When you are late, chances are it is already full. When it comes to the situation that it is required by your degree and you have to enroll it to graduate but you can't, that is no good for sure.

That's why I wrote this tiny little script to monitor the timetable page of specific courses offered by UNSW. It is understood that the enrolment status on timetable page does not reflect the real time status. There might be a 1 day delay. The most accurate way is to use myUNSW. However, that might still helps if you don't want to log on myUNSW and try your luck every now and then.

It should work fine but I have not tested it as a whole.

## Usage

Find the course id in the DOM of the timetable page. Search '1PGA' in the source code of the page and you will see. Set up your email smtp service in order to send email when the course is available. Then run it on your server.