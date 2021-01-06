import psutil 
from plyer import notification 
import time 

from datetime import datetime

now = datetime.now()

current_time = now.strftime("%H:%M:%S")


# from psutil we will import the 
# sensors_battery class and with 
# that we have the battery remaining 
while(True):
    battery = psutil.sensors_battery()
    percent = battery.percent
    if(battery.power_plugged):
        isPlugged = "Plugged!!"
    else:
        isPlugged = "Not Plugged"
    
    print(percent, ' ', isPlugged, ' ', current_time)
    
    if(percent >= 80 and battery.power_plugged):
        notification.notify( 
            title="High Charging", 
            message=str(percent)+"% Battery remaining", 
            timeout=10
        )
    elif(percent <= 15 and not battery.power_plugged):
        notification.notify( 
            title="Low Charging", 
            message=str(percent)+"% Battery remaining", 
            timeout=10
        )
	
	# after every 60 mins it will show the 
	# battery percentage 
    time.sleep(60) 
	
    continue