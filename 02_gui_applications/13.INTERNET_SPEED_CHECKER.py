import tkinter as tk
from tkinter import messagebox
import speedtest
import threading

# --- GLOBAL LAYOUT CONFIGURATIONS ---
WINDOW_WIDTH = 450
WINDOW_HEIGHT = 450
COLOR_BG = "#0F172A"       # Deep Slate Night
COLOR_CARD = "#1E293B"     # Slate Card Background
COLOR_ACCENT = "#38BDF8"   # Cyber Sky Blue
COLOR_TEXT = "#F8FAFC"     # Near White

class InternetSpeedTestGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("WsCube Tech - Internet Speed Analyzer")
        self.root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
        self.root.configure(bg=COLOR_BG)
        self.root.resizable(False, False)

        self._create_widgets()

    def _create_widgets(self):
        """Constructs the visual dashboard cards and control triggers."""
        
        # 1. Main Application Header Title Banner
        tk.Label(
            self.root, 
            text="INTERNET SPEED TEST", 
            font=("Helvetica", 16, "bold"), 
            bg=COLOR_BG, 
            fg=COLOR_TEXT
        ).pack(pady=20)

        # 2. Status Update Messaging Feed
        self.status_label = tk.Label(
            self.root,
            text="System Idle. Click below to begin diagnostics.",
            font=("Helvetica", 11, "italic"),
            bg=COLOR_BG,
            fg="#94A3B8"
        )
        self.status_label.pack(pady=5)

        # 3. Main Metric Cards Frame Container
        self.card_frame = tk.Frame(self.root, bg=COLOR_CARD, bd=1, relief="solid")
        self.card_frame.pack(pady=15, padx=45, fill="both", expand=True)

        # Download Metric Readout Row
        tk.Label(self.card_frame, text="DOWNLOAD SPEED", font=("Helvetica", 9, "bold"), bg=COLOR_CARD, fg="#64748B").pack(pady=(15, 2))
        self.download_label = tk.Label(self.card_frame, text="0.00 Mbps", font=("Helvetica", 22, "bold"), bg=COLOR_CARD, fg=COLOR_ACCENT)
        self.download_label.pack(pady=(0, 10))

        # Upload Metric Readout Row
        tk.Label(self.card_frame, text="UPLOAD SPEED", font=("Helvetica", 9, "bold"), bg=COLOR_CARD, fg="#64748B").pack(pady=(5, 2))
        self.upload_label = tk.Label(self.card_frame, text="0.00 Mbps", font=("Helvetica", 22, "bold"), bg=COLOR_CARD, fg="#F43F5E") # Rose Pink
        self.upload_label.pack(pady=(0, 10))

        # Ping Latency Readout Row
        tk.Label(self.card_frame, text="PING LATENCY", font=("Helvetica", 9, "bold"), bg=COLOR_CARD, fg="#64748B").pack(pady=(5, 2))
        self.ping_label = tk.Label(self.card_frame, text="0 ms", font=("Helvetica", 14, "bold"), bg=COLOR_CARD, fg="#10B981") # Emerald
        self.ping_label.pack(pady=(0, 15))

        # 4. Interactive Action Control Trigger Button
        # FIXED: Added the explicit .pack() positioning call directly to the widget setup!
        self.test_btn = tk.Button(
            self.root, 
            text="START SPEED TEST", 
            font=("Helvetica", 11, "bold"), 
            bg=COLOR_ACCENT, 
            fg=COLOR_BG,
            activebackground="#0EA5E9", 
            activeforeground=COLOR_BG, 
            bd=0, 
            cursor="hand2", 
            padx=40, 
            pady=12,
            command=self.launch_test_thread
        )
        self.test_btn.pack(pady=25)

    def launch_test_thread(self):
        """Spawns an asynchronous background thread to run the network testing without freezing the GUI."""
        # Update UI elements to show active state
        self.test_btn.config(state="disabled", text="TESTING IN PROGRESS...", bg="#334155")
        self.status_label.config(text="🔍 Searching for the closest server cluster...", fg=COLOR_ACCENT)
        
        self.download_label.config(text="Testing...")
        self.upload_label.config(text="Testing...")
        self.ping_label.config(text="Testing...")

        # Fire off the worker thread process
        threading.Thread(target=self.run_network_diagnostics, daemon=True).start()

    def run_network_diagnostics(self):
        """Connects to the speedtest network engine matrix to analyze metrics."""
        try:
            # Instantiate speedtest engine API hook
            st = speedtest.Speedtest()
            st.get_best_server()
            
            # 1. Download Test
            self.status_label.config(text="📥 Testing Download Bandwidth Streams...")
            raw_download = st.download()
            download_mbps = raw_download / 1_000_000  # Convert bits to Megabits
            self.download_label.config(text=f"{download_mbps:.2f} Mbps")

            # 2. Upload Test
            self.status_label.config(text="📤 Testing Upload Bandwidth Streams...")
            raw_upload = st.upload()
            upload_mbps = raw_upload / 1_000_000
            self.upload_label.config(text=f"{upload_mbps:.2f} Mbps")

            # 3. Ping Latency Metric
            ping_ms = st.results.ping
            self.ping_label.config(text=f"{int(ping_ms)} ms")

            self.status_label.config(text="✅ Network speed analysis completed!", fg="#10B981")

        except Exception as e:
            messagebox.showerror("Network Error", f"Failed to gather bandwidth diagnostics:\n{e}")
            self.status_label.config(text="❌ Test aborted due to standard connection issue.", fg="#F43F5E")
            self.download_label.config(text="0.00 Mbps")
            self.upload_label.config(text="0.00 Mbps")
            self.ping_label.config(text="0 ms")
            
        finally:
            # Re-enable the interactive action button state
            self.test_btn.config(state="normal", text="START SPEED TEST", bg=COLOR_ACCENT)

if __name__ == "__main__":
    root = tk.Tk()
    app = InternetSpeedTestGUI(root)
    root.mainloop()