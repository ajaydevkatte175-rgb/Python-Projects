import tkinter as tk
from PIL import Image, ImageTk, ImageDraw
import random
import os

# --- GLOBAL CONFIGURATIONS ---
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 400
COLOR_BG = "#2C3E50"      # Midnight Blue
COLOR_CARD = "#34495E"    # Slate Blue
COLOR_ACCENT = "#E74C3C"  # Vibrant Red
COLOR_TEXT = "#ECF0F1"    # Off-White

class DualDiceRoller:
    def __init__(self, root):
        self.root = root
        self.root.title("ROLL ROLL  - Dual Dice Simulator")
        self.root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
        self.root.configure(bg=COLOR_BG)
        self.root.resizable(False, False)

        # Ensure our assets exist before drawing layout
        self._generate_dice_assets()
        self._create_widgets()

    def _generate_dice_assets(self):
        """Creates the assets folder and generates clean dice images with visible dots."""
        if not os.path.exists("assets"):
            os.makedirs("assets")

        size = 120
        dot_radius = 8
        mid = size // 2
        l_pos, r_pos = 30, size - 30

        # Blueprint map for where dots go on a standard 6-sided dice matrix
        dot_map = {
            1: [(mid, mid)],
            2: [(l_pos, l_pos), (r_pos, r_pos)],
            3: [(l_pos, l_pos), (mid, mid), (r_pos, r_pos)],
            4: [(l_pos, l_pos), (l_pos, r_pos), (r_pos, l_pos), (r_pos, r_pos)],
            5: [(l_pos, l_pos), (l_pos, r_pos), (mid, mid), (r_pos, l_pos), (r_pos, r_pos)],
            6: [(l_pos, l_pos), (l_pos, mid), (l_pos, r_pos), (r_pos, l_pos), (r_pos, mid), (r_pos, r_pos)]
        }

        for i in range(1, 7):
            img_path = f"assets/dice{i}.png"
            if not os.path.exists(img_path):
                # Create a crisp white square with a dark border
                img = Image.new("RGB", (size, size), "#FFFFFF")
                draw = ImageDraw.Draw(img)
                draw.rectangle([0, 0, size-1, size-1], outline="#BDC3C7", width=3)
                
                # Draw the matching dots based on the map coordinates
                for cx, cy in dot_map[i]:
                    draw.ellipse([cx - dot_radius, cy - dot_radius, cx + dot_radius, cy + dot_radius], fill="#2C3E50")
                
                img.save(img_path)

    def _create_widgets(self):
        """Apparatus building structural UI elements."""
        # 1. Main Application Header Title Banner
        tk.Label(self.root, text="Dual Dice Simulator", font=("Helvetica", 22, "bold"), bg=COLOR_BG, fg=COLOR_TEXT).pack(pady=15)

        # 2. Central Frame Container displaying both Dice side-by-side
        # FIXED: Removed the invalid pading/pady parameter from inside the Frame initialization block
        self.dice_container = tk.Frame(self.root, bg=COLOR_CARD, bd=2, relief="groove")
        self.dice_container.pack(pady=20, padx=30, fill="x") # Padding is safely handled here now!

        # Left Dice Label Interface Component
        self.dice1_label = tk.Label(self.dice_container, bg=COLOR_CARD)
        self.dice1_label.pack(side="left", expand=True, pady=10)

        # Right Dice Label Interface Component
        self.dice2_label = tk.Label(self.dice_container, bg=COLOR_CARD)
        self.dice2_label.pack(side="right", expand=True, pady=10)

        # Initialize visual status display setting both dice to face value 1
        self._render_die(self.dice1_label, 1)
        self._render_die(self.dice2_label, 1)

        # 3. Dynamic Interactive Scoreboard System Output text
        self.result_label = tk.Label(self.root, text="Click below to roll both dice!", font=("Helvetica", 13, "italic"), bg=COLOR_BG, fg="#BDC3C7")
        self.result_label.pack(pady=15)

        # 4. Global Action Trigger Button Execution Call
        tk.Button(self.root, text="ROLL DICE", font=("Helvetica", 12, "bold"), bg=COLOR_ACCENT, fg=COLOR_TEXT,
                  activebackground="#C0392B", activeforeground=COLOR_TEXT, cursor="hand2", bd=0, padx=25, pady=8,
                  command=self.roll_dice_action).pack(pady=10)

    def _render_die(self, target_label, value):
        """Loads and anchors PhotoImage instance safely onto targeted widget labels."""
        pil_img = Image.open(f"assets/dice{value}.png")
        tk_img = ImageTk.PhotoImage(pil_img)
        
        target_label.config(image=tk_img)
        target_label.image = tk_img  # Crucial memory reference anchor point

    def roll_dice_action(self):
        """Generates two distinct random results and pushes updates to the GUI pipeline."""
        roll1 = random.randint(1, 6)
        roll2 = random.randint(1, 6)

        # Re-render both image objects with their new corresponding values
        self._render_die(self.dice1_label, roll1)
        self._render_die(self.dice2_label, roll2)

        # Update text metrics tracking total output scores achieved
        self.result_label.config(
            text=f"You rolled: {roll1} & {roll2} (Total Score: {roll1 + roll2})",
            font=("Helvetica", 13, "bold"),
            fg="#2ECC71"
        )

if __name__ == "__main__":
    root = tk.Tk()
    app = DualDiceRoller(root)
    root.mainloop()