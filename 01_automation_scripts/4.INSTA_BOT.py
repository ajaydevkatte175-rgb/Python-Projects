# =====================================================================
# 1. CRITICAL PYTHON 3.13 PATCH (Fixes missing 'imghdr' module error)
# =====================================================================
import sys
import types

fake_imghdr = types.ModuleType("imghdr")
fake_imghdr.what = lambda filename, h=None: None
sys.modules["imghdr"] = fake_imghdr
# =====================================================================

from instabot import Bot
import os
import shutil

def run_instagram_bot():
    print("Initializing Instagram Automation Engine...")

    # --- CLEANUP UTILITY ---
    # instabot creates a 'config' folder on login. If a previous run crashed,
    # this folder prevents a new login. We clear it automatically.
    if os.path.exists("config"):
        try:
            shutil.rmtree("config")
            print("Cleared old session cache configuration successfully.")
        except Exception as e:
            print(f"Note: Could not clear config folder automatically: {e}")

    # --- INITIALIZE BOT ---
    bot = Bot()

    # --- CREDENTIALS ---
    # Replace with your actual test account details
    USERNAME = "jackbelfort07"
    PASSWORD = "Ajay@1754"

    try:
        print("Attempting connection authorization to Instagram servers...")
        bot.login(username=USERNAME, password=PASSWORD)
        print("Login Successful!")

        # --- AUTOMATION ACTIONS ---
        # Action A: Follow a specific user
        target_user = "riteshhh_111"
        bot.follow(target_user)
        print(f"Successfully followed user: {target_user}")

        # Action B: Upload a photo with a caption
        # Ensure 'qr_code.png' actually exists in your project folder!
        if os.path.exists("qr_code.png"):
            bot.upload_photo("qr_code.png", caption="Automated post using Python! 🐍📸")
            print("Photo uploaded successfully.")
        else:
            print("Skipping upload: 'qr_code.png' asset not found in directory.")

        # Action C: Send a direct message (DM)
        bot.send_message("Hello from Python!", [target_user])
        print(f"Message dispatched cleanly to {target_user}")

    except Exception as e:
        print(f"An operational error occurred during automation execution: {e}")

if __name__ == "__main__":
    run_instagram_bot()