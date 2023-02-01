import time

def countdown(time_sec):
    while time_sec:
        mins, secs = divmod(time_sec, 60) # Seconds to minutes
        timeformat = '{:02d}:{:02d}'.format(mins, secs) # formating output in mins and secs
        print(timeformat, end = '\r') # Displaying output on the screen
        time.sleep(1) # timer sleeps when time is one second
        time_sec -= 1 # Decrements each second from the time remaining

        print('stop')


num = int(input("Set your time in sec: "))
countdown(num)
