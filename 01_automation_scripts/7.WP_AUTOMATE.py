import pywhatkit as kit
import datetime
import time

def send_automated_whatsapp():
    print("Initializing WhatsApp Automation Engine...")
    
    # --- CONFIGURATIONS ---
    # Target phone number (Must include country code, e.g., +91 for India)
    phone_number = "+918378883369" 
    message = "Hello! This is an automated message sent using Python. 🐍🤖"
    
    # --- TIME CALCULATIONS ---
    # Fetch the current system time
    now = datetime.datetime.now()
    
    # Schedule the message to go out exactly 2 minutes from right now
    schedule_time = now + datetime.timedelta(minutes=2)
    schedule_hour = schedule_time.hour
    schedule_minute = schedule_time.minute
    
    print(f"Current Time: {now.strftime('%H:%M')}")
    print(f"Message scheduled for: {schedule_hour:02d}:{schedule_minute:02d}")
    print("Please ensure WhatsApp Web is logged in on your default browser.")
    
    try:
        # Core API Execution Call:
        # Parameters: phone_no, message, time_hour, time_min, wait_time(secs)
        kit.sendwhatmsg(
            phone_no=phone_number,
            message=message,
            time_hour=schedule_hour,
            time_min=schedule_minute,
            wait_time=15  # Gives the browser 15 seconds to open and load completely
        )
        print("Browser triggered successfully! Message will send momentarily.")
        
    except Exception as e:
        print(f"An unexpected operational error occurred: {e}")

if __name__ == "__main__":
    send_automated_whatsapp()