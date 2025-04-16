import time

seconds = int(input("Enter time in seconds: "))

while seconds:
    mins, secs = divmod(seconds, 60)
    timer = f'{mins:02d}:{secs:02d}'
    print(timer, end='\r')  # '\r' to overwrite the line
    time.sleep(1)
    seconds -= 1

print("⏰ Time's up!")
