# --- Ambientlight Cycle for SenseHat  by Wladimir Delenclos


#--- Requis 
from sense_hat import SenseHat
import time
import sys
from time import gmtime, strftime
from evdev import InputDevice, ecodes,list_devices
import os


# --- Demarrage 
sense = SenseHat()
sense.load_image("hello.png")
hour = int(float(strftime("%H")));

def spinning_cursor():
    while True:
        for cursor in '|/-\\':
            yield cursor
spinner = spinning_cursor()

print ("\n\n\n############# Ambientlight Cycle for SenseHat ###########")
print ("#\n#")
print ("\n_________________________")
print ("\nVersion 0.1 | Documentation: https://github.com/wladouche/")
for _ in range(50):
    sys.stdout.write(spinner.next())
    sys.stdout.flush()
    time.sleep(0.1)
    sys.stdout.write('\b')

try:
    while True:
        month = time.strftime("%b") 
        if( month == "Oct" or month == "Nov" or month == "Dec" or month == "Jan" or month == "Feb" or month == "Mar"):
            if(hour == 5):
                    sense.clear()
                    sense.load_image("night.png")

            elif(hour == 6):
                    sense.clear()
                    sense.load_image("PrePastNight.png")

            elif(hour == 7):
                    sense.clear()
                    sense.load_image("Transit0.png")

            elif(hour == 8):
                    sense.clear()
                    sense.load_image("Transit1.png")

            elif(hour == 9):
                    sense.clear()
                    sense.load_image("Transit2.png")

            elif(hour == 10):
                    sense.clear()
                    sense.load_image("Transit3.png")

            elif(hour == 12):
                    sense.clear()
                    sense.load_image("Full.png")

            elif(hour == 15):                
                    sense.clear()
                    sense.load_image("PastFull.png")

            elif(hour == 16):
                    sense.clear()
                    sense.load_image("Transit2.png")

            elif(hour == 17):
                    sense.clear()
                    sense.load_image("Transit1.png")  

            elif(hour == 18):
                    sense.clear()
                    sense.load_image("Transit0.png")

            elif(hour == 19 or hour == 20):
                    sense.clear()
                    sense.load_image("PrePastNight.png") 

            elif(hour >= 21):
                    sense.clear()
                    sense.load_image("night.png")
        else:
            if(hour == 5):
                    sense.clear()
                    sense.load_image("night.png")

            elif(hour == 6):
                    sense.clear()
                    sense.load_image("PrePastNight.png")

            elif(hour == 7):
                    sense.clear()
                    sense.load_image("Transit0.png")

            elif(hour == 8):
                    sense.clear()
                    sense.load_image("Transit1.png")

            elif(hour == 9):
                    sense.clear()
                    sense.load_image("Transit2.png")

            elif(hour == 10):
                    sense.clear()
                    sense.load_image("Transit3.png")

            elif(hour == 12 or hour == 13 or hour == 14):
                    sense.clear()
                    sense.load_image("Full.png")

            elif(hour == 15):                
                    sense.clear()
                    sense.load_image("PastFull.png")

            elif(hour == 18):
                    sense.clear()
                    sense.load_image("Transit2.png")

            elif(hour == 19):
                    sense.clear()
                    sense.load_image("Transit1.png")  

            elif(hour == 20):
                    sense.clear()
                    sense.load_image("Transit0.png")

            elif(hour == 21):
                    sense.clear()
                    sense.load_image("PrePastNight.png") 

            elif(hour >= 22):
                    sense.clear()
                    sense.load_image("night.png")         

        tFromHumidity = sense.get_temperature_from_humidity()
        tFromPressure = sense.get_temperature_from_pressure()
        
        print "Humidite: " + str( tFromHumidity*0.67) + "%"
        print "Temperature (depuis la pression): " + str(tFromPressure) + " degresC" 
        print "Temperature: " + str(sense.get_temperature()) + " degres C"
        print "Pression: " +  str(sense.get_pressure()) + " millibar"
        print ("\nMois en cours: " + time.strftime("%b"))
        print ("\nHeure du check: " + time.strftime("%H"))
        print ("\nCtrl+C pour arreter")
        print ("\n____________________________________________\n")
        time.sleep(10)

except KeyboardInterrupt:
    sense.load_image("off.png")
    print "Au revoir !"
    try:
        sys.exit(0)
    except SystemExit:
        os._exit(0)

