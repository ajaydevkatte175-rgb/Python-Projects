from tkinter import Label, Tk 
import time

# --- MAIN APPLICATION CORE INITIALIZATION ---
app_window = Tk() 
app_window.title("Digital Clock Studio") 
app_window.geometry("440x160") 
app_window.resizable(False, False) 

# --- DESIGN PARAMETERS ---
text_font = ("Helvetica", 48, 'bold')
background = "#0F172A"  
foreground = "#38BDF8"  
border_width = 20

# --- UI COMPONENTS ---
label = Label(
    app_window, 
    font=text_font, 
    bg=background, 
    fg=foreground, 
    bd=border_width
) 
label.pack(expand=True, fill="both")

def digital_clock(): 
    """Queries the OS system runtime clock to pull fresh time string data."""
    time_live = time.strftime("%H:%M:%S")
    label.config(text=time_live) 
    label.after(200, digital_clock)

# Fire up the initial pipeline execution sequence 
digital_clock()

# Run the persistent window thread manager
# app_window.mainloop()