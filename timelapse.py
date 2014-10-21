import ephem
import datetime
import time
import os

sun = ephem.Sun()

Cambridge = ephem.Observer()
Cambridge.lat = '55.676111'
Cambridge.lon = '12.568333'
Cambridge.date = datetime.datetime.now()

sunrise = ephem.localtime(Cambridge.next_rising(sun))
sunset = ephem.localtime(Cambridge.next_setting(sun))

while True:
    while sunrise < datetime.datetime.now() < sunset:
        print('Its the daytime!')
        print('Take a photo!')
        os.system('raspistill -o {}.jpg'.format(datetime.datetime.now().strftime('%y-%m-%d %H:%M')))
        time.sleep(1800)
    print('Its nighttime!')
    Cambridge.date = datetime.datetime.now()

    sunrise = ephem.localtime(Cambridge.next_rising(sun))
    sunset = ephem.localtime(Cambridge.next_setting(sun))

    time.sleep((sunrise - datetime.datetime.now()).total_seconds())