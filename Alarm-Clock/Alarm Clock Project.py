import datetime
import time
import winsound

alarm_time = input("Enter alarm time (HH:MM):  ")

while True:
    current_time =datetime.datetime.now().strftime("%H:%M")
    
   
    if current_time == alarm_time:
        print ("⏰ Alarm!")

        for i in range(3,0,-1):
            print(i)
            time.sleep(1)
        
        winsound.Beep(1500,800)    #First number is the frequency(pitch) and second number is the duration in milliseconds
        print(""" 🚨🚨🚨
                  Wake Up!
                  🚨🚨🚨""")
        
        break
    time.sleep(1)

    