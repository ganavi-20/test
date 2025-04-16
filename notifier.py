from plyer import notification
import time
def send_notification(title, message, timeout=10):
    notification.notify(
        title=title,
        message=message,
        timeout=timeout)
