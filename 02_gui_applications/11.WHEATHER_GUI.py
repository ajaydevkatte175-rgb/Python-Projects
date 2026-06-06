import tkinter as tk
from tkinter import ttk, messagebox
import requests

# --- GLOBAL CONFIGURATIONS ---
WINDOW_WIDTH = 450
WINDOW_HEIGHT = 400
COLOR_BG = "#111827"       # Deep Charcoal Night
COLOR_CARD = "#1F2937"     # Dark Slate Grey
COLOR_ACCENT = "#10B981"   # Emerald Green
COLOR_TEXT = "#F9FAFB"     # Crisp White

class WeatherAppGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("WsCube Tech - Weather Analytics")
        self.root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
        self.root.configure(bg=COLOR_BG)
        self.root.resizable(False, False)

        self._create_widgets()

    def _create_widgets(self):
        """Constructs visual dashboard layouts."""
        
        # 1. Title Header Banner View
        tk.Label(
            self.root, 
            text="Weather Analytics Dashboard", 
            font=("Helvetica", 18, "bold"), 
            bg=COLOR_BG, 
            fg=COLOR_TEXT
        ).pack(pady=20)

        # 2. Input Box Control Frame Panel Row
        input_frame = tk.Frame(self.root, bg=COLOR_BG)
        input_frame.pack(pady=10, padx=30, fill="x")

        self.city_entry = tk.Entry(
            input_frame, 
            font=("Helvetica", 14), 
            bg=COLOR_CARD, 
            fg=COLOR_TEXT, 
            insertbackground=COLOR_TEXT, 
            bd=0, 
            highlightthickness=1,
            highlightbackground="#374151"
        )
        self.city_entry.pack(side="left", fill="x", expand=True, ipady=5, padx=5)
        self.city_entry.insert(0, "Mumbai")  # Default placeholder value
        self.city_entry.bind("<Return>", lambda event: self.fetch_weather_pipeline())

        search_btn = tk.Button(
            input_frame, 
            text="SEARCH", 
            font=("Helvetica", 10, "bold"), 
            bg=COLOR_ACCENT, 
            fg=COLOR_TEXT,
            activebackground="#059669", 
            activeforeground=COLOR_TEXT, 
            bd=0, 
            cursor="hand2", 
            padx=15,
            command=self.fetch_weather_pipeline
        )
        search_btn.pack(side="right", padx=5)

        # 3. Main Data Core Metrical Display Box Frame Panel
        self.display_card = tk.Frame(self.root, bg=COLOR_CARD, bd=1, relief="solid", highlightthickness=0)
        self.display_card.pack(pady=20, padx=35, fill="both", expand=True)

        # Metrics Internal Text Variable Fields Labels
        self.city_label = tk.Label(self.display_card, text="City Name, CC", font=("Helvetica", 16, "bold"), bg=COLOR_CARD, fg=COLOR_TEXT)
        self.city_label.pack(pady=(15, 5))

        self.temp_label = tk.Label(self.display_card, text="--°C", font=("Helvetica", 32, "bold"), bg=COLOR_CARD, fg=COLOR_ACCENT)
        self.temp_label.pack(pady=5)

        self.desc_label = tk.Label(self.display_card, text="Clear Sky", font=("Helvetica", 12, "italic"), bg=COLOR_CARD, fg="#9CA3AF")
        self.desc_label.pack(pady=5)

        self.humidity_label = tk.Label(self.display_card, text="Humidity: --%", font=("Helvetica", 11), bg=COLOR_CARD, fg="#D1D5DB")
        self.humidity_label.pack(pady=(5, 15))

    def fetch_weather_pipeline(self):
        """Extracts text, triggers network pipeline actions, and maps output parameters safely."""
        city = self.city_entry.get().strip()
        
        if not city:
            messagebox.showwarning("Input Required", "Please enter a valid city name first!")
            return

        # Target Endpoint: Open public fallback geolocation testing matrix endpoint API
        api_url = f"https://wttr.in/{city}?format=j1"

        try:
            # Dispatch network request stream channel
            response = requests.get(api_url, timeout=10)
            
            if response.status_code == 404:
                messagebox.showerror("Not Found", f"City '{city}' could not be pinpointed.")
                return
                
            # Unroll complex nested JSON response string payload mapping parameters back out
            weather_data = response.json()
            
            # Navigate the JSON object matrix path arrays
            current_condition = weather_data['current_condition'][0]
            nearest_area = weather_data['nearest_area'][0]
            
            # Isolate raw metrics data values 
            temp_c = current_condition['temp_C']
            humidity = current_condition['humidity']
            description = current_condition['weatherDesc'][0]['value']
            city_found = nearest_area['areaName'][0]['value']
            country_found = nearest_area['country'][0]['value']

            # Update Graphic Dashboard State Elements 
            self.city_label.config(text=f"{city_found}, {country_found}")
            self.temp_label.config(text=f"{temp_c}°C")
            self.desc_label.config(text=description.title())
            self.humidity_label.config(text=f"Humidity: {humidity}%")

        except requests.exceptions.ConnectionError:
            messagebox.showerror("Connection Failure", "No internet connection detected. Please verify your connection stream channel.")
        except Exception as e:
            messagebox.showerror("Operational Failure", f"An error occurred parsing weather data metrics:\n{e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = WeatherAppGUI(root)
    root.mainloop()