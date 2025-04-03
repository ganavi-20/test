def alarm_clock():
    alarm_time = input("Enter the time for the alarm (HH:MM): ")

    while True:
        current_time = time.strftime("%H:%M")
        print(f"Current Time: {current_time}", end="\r")
        time.sleep(1)

        if current_time == alarm_time:
            print(f"\nAlarm! It's {alarm_time}. Time to wake up!")
            break

alarm_clock()
