# enrolment-monitor
### Background

Some popular courses in UNSW is hard to enroll in. When you are late, chances are it is already full. When it comes to the situation that it is required by your degree and you have to enroll it to graduate but you can't, that is no good for sure.

That's why I wrote this tiny little script to monitor the timetable page of specific courses offered by UNSW. It is understood that the enrolment status on timetable page does not reflect the real time status. There might be a 1 day delay. The most accurate way is to use myUNSW. However, that might still helps if you don't want to log on myUNSW and try your luck every now and then.

It should work fine but I have not successfully used it:( The course is always full.

## Usage

`pip install -r requirements.txt`

Read the source code. Look for where you should modify the code. Especially the SMTP settings and the actual parameter to track the course.

I could make it more user friendly like when you provide a course code and the desired term as the attributes and the program would execute directly. Butttttt I am lazy :) If you can find this, you more or less know something about scripting and can figure it out yourself.

Please use it with consideration of others!