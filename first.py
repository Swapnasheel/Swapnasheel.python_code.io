import webbrowser
import time



time_count = 3
break_count = 0

print "Program started at " + time.ctime()

while(break_count < time_count):
    time.sleep(5)
    webbrowser.open("https://www.youtube.com/watch?v=gwZJ-R-Q_eo")
    break_count = break_count + 1

    
