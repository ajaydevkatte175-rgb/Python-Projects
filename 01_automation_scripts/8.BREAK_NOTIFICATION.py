import time
from plyer import notification
import sys

def start_break_notifier():
    # --- CONFIGURATIONS ---
    # Set the break interval (e.g., remind every 45 minutes)
    # For testing purposes, we set this to 10 seconds so you can see it work immediately!
    BREAK_INTERVAL_SECONDS = 10 
    
    print("=============================================")
    print("   DESKTOP NOTIFICATION SYSTEM INITIALIZED   ")
    print("=============================================")
    print(f"Engine running... Reminders active every {BREAK_INTERVAL_SECONDS} seconds.")
    print("Press Ctrl + C in the terminal to terminate the background process.\n")

    reminder_count = 0

    # Continuous loop keeping the script alive in the background
    while True:
        try:
            # Put the script to sleep. This uses 0% CPU while waiting!
            time.sleep(BREAK_INTERVAL_SECONDS)
            
            reminder_count += 1
            
            # --- TRIGGER NATIVE OS NOTIFICATION ---
            notification.notify(
                title="🚨 Take a Break! 🚨",
                message=f"You've been working hard. Stand up, stretch your legs, and rest your eyes!\n(Reminder #{reminder_count})",
                app_name="HealthNotifier",
                
                # Optional: Path to a .ico file (Windows) or .png (Mac) for a custom icon
                # app_icon="assets/health_icon.ico", 
                
                timeout=6  # The notification banner stays on screen for 6 seconds
            )
            print(f"[{time.strftime('%H:%M:%S')}] Reminder #{reminder_count} dispatched to desktop.")
            
        except KeyboardInterrupt:
            # Graceful exit handling when the user presses Ctrl + C
            print("\nShutting down Break Notifier Engine... Stay healthy!")
            sys.exit()
            
        except Exception as e:
            print(f"An unexpected operational error occurred: {e}")
            break

if __name__ == "__main__":
    start_break_notifier()