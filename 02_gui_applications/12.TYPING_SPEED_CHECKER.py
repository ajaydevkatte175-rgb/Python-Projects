import tkinter as tk
from tkinter import messagebox
import random
import time

# --- GLOBAL CONFIGURATIONS ---
WINDOW_WIDTH = 550
WINDOW_HEIGHT = 500
COLOR_BG = "#0F172A"       # Deep Slate Blue
COLOR_CARD = "#1E293B"     # Dark Card Background
COLOR_ACCENT = "#38BDF8"   # Cyber Sky Blue
COLOR_TEXT = "#F8FAFC"     # Near White

# Sample sentences bank for the test framework
TEST_SENTENCES = [
    "The quick brown fox jumps over the lazy dog.",
    "Python is an amazing programming language for beginners.",
    "Practice makes perfect when learning to type fast.",
    "Always write clean, readable, and well-documented code.",
    "Tkinter makes building desktop graphical user interfaces fun."
]

class TypingSpeedCheckerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("WsCube Tech - Typing Speed Analytics")
        self.root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
        self.root.configure(bg=COLOR_BG)
        self.root.resizable(False, False)

        # Operational State Variables
        self.start_time = 0
        self.target_text = ""
        self.is_running = False

        self._create_widgets()

    def _create_widgets(self):
        """Constructs visual typing test metric panels."""
        
        # 1. Main Title Header Banner (FIXED: -letterspacing option completely removed)
        tk.Label(
            self.root, 
            text="TYPING SPEED ANALYTICS", 
            font=("Helvetica", 16, "bold"), 
            bg=COLOR_BG, 
            fg=COLOR_TEXT
        ).pack(pady=15)

        # 2. Status Instruction Label
        self.status_label = tk.Label(
            self.root,
            text="Click the button below to start the test!",
            font=("Helvetica", 11, "italic"),
            bg=COLOR_BG,
            fg="#94A3B8"
        )
        self.status_label.pack(pady=5)

        # 3. Main Text Showcase Panel Card (Displays sentence to type)
        self.card_frame = tk.Frame(self.root, bg=COLOR_CARD, bd=1, relief="solid")
        self.card_frame.pack(pady=10, padx=30, fill="x")

        self.sentence_label = tk.Label(
            self.card_frame, 
            text="Press Start to load sentence...", 
            font=("Helvetica", 12, "bold"), 
            bg=COLOR_CARD, 
            fg=COLOR_ACCENT,
            wraplength=450,
            justify="center"
        )
        self.sentence_label.pack(pady=25, padx=15)

        # 4. User Text Input Frame Workspace
        tk.Label(self.root, text="TYPE THE SENTENCE BELOW:", font=("Helvetica", 10, "bold"), bg=COLOR_BG, fg="#64748B").pack(anchor="w", padx=35, pady=(10, 2))
        
        self.input_box = tk.Text(
            self.root, 
            wrap="word", 
            height=4, 
            bg=COLOR_CARD, 
            fg=COLOR_TEXT, 
            bd=0, 
            font=("Helvetica", 12),
            state="disabled", # Locked until start button is clicked
            highlightthickness=1,
            highlightbackground="#334155"
        )
        self.input_box.pack(fill="x", padx=30, pady=5)
        # Bind key release to continuously check accuracy and speed while typing
        self.input_box.bind("<KeyRelease>", self.evaluate_realtime_performance)

        # 5. Live Live Scoreboard Metrics Row
        self.metrics_frame = tk.Frame(self.root, bg=COLOR_BG)
        self.metrics_frame.pack(pady=15)

        self.wpm_label = tk.Label(self.metrics_frame, text="WPM: --", font=("Helvetica", 14, "bold"), bg=COLOR_BG, fg="#10B981")
        self.wpm_label.pack(side="left", padx=20)

        self.accuracy_label = tk.Label(self.metrics_frame, text="Accuracy: --%", font=("Helvetica", 14, "bold"), bg=COLOR_BG, fg="#F43F5E")
        self.accuracy_label.pack(side="right", padx=20)

        # 6. Action Control Activation Trigger Button
        self.action_btn = tk.Button(
            self.root, 
            text="START TYPING TEST", 
            font=("Helvetica", 11, "bold"), 
            bg=COLOR_ACCENT, 
            fg=COLOR_BG,
            activebackground="#0EA5E9", 
            activeforeground=COLOR_BG, 
            bd=0, 
            cursor="hand2", 
            padx=30, 
            pady=12,
            command=self.start_typing_test_pipeline
        )
        self.action_btn.pack(pady=15)

    def start_typing_test_pipeline(self):
        """Initializes state thresholds, picks a sentence, and unlocks inputs."""
        self.target_text = random.choice(TEST_SENTENCES)
        self.sentence_label.config(text=self.target_text, fg=COLOR_TEXT)
        
        # Reset and activate input field state properties
        self.input_box.config(state="normal", highlightbackground=COLOR_ACCENT)
        self.input_box.delete("1.0", "end")
        self.input_box.focus_set()
        
        # Reset visual metrics readouts
        self.wpm_label.config(text="WPM: 0")
        self.accuracy_label.config(text="Accuracy: 100%")
        self.status_label.config(text="⚡ Type as fast and accurately as you can!", fg=COLOR_ACCENT)
        
        # Lock internal timer anchors
        self.start_time = time.time()
        self.is_running = True
        
        # Transform structural button configuration into a working Reset channel
        self.action_btn.config(text="RESTART TEST", bg="#64748B")

    def evaluate_realtime_performance(self, event):
        """Monitors keystroke entries real-time to compute accuracy parameters."""
        if not self.is_running:
            return

        # Read typed values out from Tkinter text workspace matrix bounds cleanly
        typed_text = self.input_box.get("1.0", "end-1c")
        elapsed_time = time.time() - self.start_time

        # Prevent division-by-zero errors if key is hit instantly on second zero 
        if elapsed_time == 0:
            elapsed_time = 0.001

        # Calculate Accuracy Matrix
        correct_chars = 0
        min_length = min(len(typed_text), len(self.target_text))
        
        for i in range(min_length):
            if typed_text[i] == self.target_text[i]:
                correct_chars += 1

        accuracy = (correct_chars / len(typed_text)) * 100 if len(typed_text) > 0 else 100
        self.accuracy_label.config(text=f"Accuracy: {int(accuracy)}%")

        # Calculate Words Per Minute (Standard: 1 word = 5 character slots)
        words = len(typed_text) / 5
        minutes = elapsed_time / 60
        wpm = words / minutes
        self.wpm_label.config(text=f"WPM: {int(wpm)}")

        # Check Termination Criteria (Did the user type the whole sentence?)
        if len(typed_text) >= len(self.target_text):
            self.is_running = False
            self.input_box.config(state="disabled", highlightbackground="#334155")
            self.status_label.config(text="🎉 Test complete! Excellent job.", fg="#10B981")
            self.action_btn.config(text="START NEW TEST", bg=COLOR_ACCENT)
            
            # Show terminal metrics results dialog popup box wrap
            messagebox.showinfo("Test Results", f"🏁 Final Score Metrics:\n\n🚀 Speed: {int(wpm)} WPM\n🎯 Accuracy: {int(accuracy)}%")

if __name__ == "__main__":
    root = tk.Tk()
    app = TypingSpeedCheckerGUI(root)
    root.mainloop()