import ephem
import datetime
import time
import os

sun = ephem.Sun()

Cambridge = ephem.Observer()
Cambridge.lat = '52.205'
Cambridge.lon = '0.119'
Cambridge.elev = 6
Cambridge.date = datetime.datetime.now()

sunrise = ephem.localtime(Cambridge.next_rising(sun))
sunset = ephem.localtime(Cambridge.next_setting(sun))

while True:
    while sunrise < datetime.datetime.now() < sunset or datetime.datetime.now() < sunset < sunrise:
        os.system('raspistill -o {}.jpg'.format(datetime.datetime.now().strftime('%y-%m-%d\ %H:%M')))
        time.sleep(1800)
    Cambridge.date = datetime.datetime.now()

    sunrise = ephem.localtime(Cambridge.next_rising(sun))
    sunset = ephem.localtime(Cambridge.next_setting(sun))

    time.sleep((sunrise - datetime.datetime.now()).total_seconds())
