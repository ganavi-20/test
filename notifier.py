from plyer import notification
import time
def send_notification(title, message, timeout=10):
    notification.notify(
        title=title,
        message=message,
        timeout=timeout)
    print("Desktop Notifier started...")


interval = 5  
title = "Reminder"
message = "This is your notification reminder!"
time.sleep(interval)  # Wait for the interval time
send_notification(title, message)

print("Notification sent!")
