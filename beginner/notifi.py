import psutil
from plyer import notification

battery=psutil.sensors_battery()
percent,plugged=battery.percent,battery.power_plugged



if __name__=='__main__':
    if plugged:
        notification.notify(title='Reminder',message='message',timeout=10)
    else:
        notification.notify(title='No reminder',message='mess',timeout=10)