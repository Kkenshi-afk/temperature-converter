import time
def alarm(countdown):
    print(f"Countdown for {countdown} seconds starting...")
    while countdown > 0:
        print(countdown)
        time.sleep(1)  
        countdown -= 1
    
    print("⏰ Alarm is ringing!")
try:
    seconds = int(input("How many seconds until the alarm rings? "))
    alarm(seconds)
except ValueError:
    print("Please enter number!")
