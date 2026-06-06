import tkinter as tk
from tkinter import ttk, messagebox
from deep_translator import GoogleTranslator

# --- GLOBAL LAYOUT CONFIGURATIONS ---
WINDOW_WIDTH = 650
WINDOW_HEIGHT = 450
COLOR_BG = "#1E293B"       # Slate Blue Dark
COLOR_CARD = "#334155"     # Slate Blue Medium
COLOR_ACCENT = "#3B82F6"   # Electric Blue Button
COLOR_TEXT = "#F8FAFC"     # Near White

class LanguageTranslatorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Google Translator Studio")
        self.root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
        self.root.configure(bg=COLOR_BG)
        self.root.resizable(False, False)

        # Dictionary mapping display names to ISO codes
        self.language_map = {
            "Detect Language (Auto)": "auto",
            "Hindi": "hi",
            "Spanish": "es",
            "French": "fr",
            "German": "de",
            "Arabic": "ar",
            "Japanese": "ja",
            "Italian": "it",
            "Russian": "ru"
        }

        self._create_widgets()

    def _create_widgets(self):
        """Constructs and grids visual dashboard components."""
        
        # 1. Title Banner
        title_label = tk.Label(
            self.root, 
            text="Language Translation Studio", 
            font=("Helvetica", 18, "bold"), 
            bg=COLOR_BG, 
            fg=COLOR_TEXT
        )
        title_label.pack(pady=15)

        # 2. Control Panel Box (Language Dropdowns Selection)
        control_frame = tk.Frame(self.root, bg=COLOR_BG)
        control_frame.pack(pady=10, fill="x", padx=30)

        # Source Language Selector Combo Box
        tk.Label(control_frame, text="From:", font=("Helvetica", 11), bg=COLOR_BG, fg="#94A3B8").pack(side="left", padx=5)
        self.src_lang_combo = ttk.Combobox(control_frame, values=list(self.language_map.keys()), state="readonly", width=22)
        self.src_lang_combo.pack(side="left", padx=5)
        self.src_lang_combo.set("Detect Language (Auto)")

        # Target Language Selector Combo Box
        self.dest_lang_combo = ttk.Combobox(control_frame, values=list(self.language_map.keys())[1:], state="readonly", width=22)
        self.dest_lang_combo.pack(side="right", padx=5)
        self.dest_lang_combo.set("Hindi")
        tk.Label(control_frame, text="To:", font=("Helvetica", 11), bg=COLOR_BG, fg="#94A3B8").pack(side="right", padx=5)

        # 3. Main Text IO Splitting Workspace Frame
        workspace_frame = tk.Frame(self.root, bg=COLOR_BG)
        workspace_frame.pack(pady=15, fill="both", expand=True, padx=30)

        # Left Column Container: Input Area
        input_container = tk.Frame(workspace_frame, bg=COLOR_BG)
        input_container.pack(side="left", fill="both", expand=True, padx=5)
        
        tk.Label(input_container, text="Source Text", font=("Helvetica", 10, "bold"), bg=COLOR_BG, fg="#64748B").pack(anchor="w")
        self.input_text_box = tk.Text(input_container, wrap="word", height=8, width=25, bg=COLOR_CARD, fg=COLOR_TEXT, bd=0, font=("Helvetica", 11))
        self.input_text_box.pack(fill="both", expand=True, pady=5)

        # Right Column Container: Output Area
        output_container = tk.Frame(workspace_frame, bg=COLOR_BG)
        output_container.pack(side="right", fill="both", expand=True, padx=5)
        
        tk.Label(output_container, text="Translation Output", font=("Helvetica", 10, "bold"), bg=COLOR_BG, fg="#64748B").pack(anchor="w")
        self.output_text_box = tk.Text(output_container, wrap="word", height=8, width=25, bg=COLOR_CARD, fg="#2ECC71", bd=0, font=("Helvetica", 11, "bold"), state="disabled")
        self.output_text_box.pack(fill="both", expand=True, pady=5)

        # 4. Global Action Trigger Button
        translate_btn = tk.Button(
            self.root, 
            text="TRANSLATE TEXT", 
            font=("Helvetica", 12, "bold"), 
            bg=COLOR_ACCENT, 
            fg=COLOR_TEXT,
            activebackground="#2563EB", 
            activeforeground=COLOR_TEXT, 
            bd=0, 
            cursor="hand2", 
            padx=40, 
            pady=10,
            command=self.execute_translation_pipeline
        )
        translate_btn.pack(pady=20)

    def execute_translation_pipeline(self):
        """Extracts source payload metadata strings and fires background network actions."""
        # Extract plain-text string values out from Tkinter Text Object bounds safely
        raw_text = self.input_text_box.get("1.0", "end-1c").strip()
        
        if not raw_text:
            messagebox.showwarning("Empty Input", "Please type or paste some text to translate first!")
            return

        # Map display selection choices back down into ISO tokens
        src_iso = self.language_map[self.src_lang_combo.get()]
        dest_iso = self.language_map[self.dest_lang_combo.get()]

        try:
            # Set up the API wrapper pipeline interface 
            translator = GoogleTranslator(source=src_iso, target=dest_iso)
            translated_result = translator.translate(raw_text)

            # Mutate state parameters on Output Display box dynamically
            self.output_text_box.config(state="normal")      # Unlock edit protections 
            self.output_text_box.delete("1.0", "end")         # Clear past old string cache
            self.output_text_box.insert("1.0", translated_result) # Inject fresh values 
            self.output_text_box.config(state="disabled")    # Re-engage security locks

        except Exception as e:
            messagebox.showerror("Gateway Error", f"Failed to reach translation cloud service:\n{e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = LanguageTranslatorGUI(root)
    root.mainloop()