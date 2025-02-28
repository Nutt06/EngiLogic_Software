import tkinter as tk
import random

# Thai consonants and their names
thai_consonants = [
    ("ก", "Gor Gai"), ("\u0e02", "Khor Khai"), ("\u0e03", "Khor Khuat"),
    ("\u0e04", "Khor Khwai"), ("\u0e05", "Khor Khon"), ("\u0e06", "Khor Rakhang"),
    ("\u0e07", "Ngor Ngu"), ("\u0e08", "Jor Jan"), ("\u0e09", "Chor Ching"),
    ("\u0e0a", "Chor Chang"), ("\u0e0b", "Sor So"), ("\u0e0c", "Chor Cher"),
    ("\u0e0d", "Yor Ying"), ("\u0e0e", "Dor Chada"), ("\u0e0f", "Tor Patak"),
    ("\u0e10", "Thor Thung"), ("\u0e11", "Thor Thahan"), ("\u0e12", "Thor Thong"),
    ("\u0e13", "Nor Nenu"), ("\u0e14", "Dor Dek"), ("\u0e15", "Tor Tao"),
    ("\u0e16", "Thor Tho"), ("\u0e17", "Thor Phu Thao"), ("\u0e18", "Nor Nen"),
    ("\u0e19", "Bor Baimai"), ("\u0e1a", "Por Pla"), ("\u0e1b", "For Fun"),
    ("\u0e1c", "Por Phan"), ("\u0e1d", "For Samphao"), ("\u0e1e", "Mor Ma"),
    ("\u0e1f", "Yor Yak"), ("\u0e20", "Ror Rua"), ("\u0e21", "Lor Ling"),
    ("\u0e22", "Sor Sala"), ("\u0e23", "Sor Rusi"), ("\u0e24", "Sor Suea"),
    ("\u0e25", "Hor Hip"), ("\u0e26", "Lor Chula"), ("\u0e27", "Or Ang"),
    ("\u0e28", "Hor Nokhuk"), ("\u0e29", "Hor Nam"), ("\u0e2a", "Lor Ching")
]

class FlashcardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Thai Consonant Flashcards")
        self.root.geometry("400x300")
        
        self.card_frame = tk.Frame(root, width=400, height=300, bg="white")
        self.card_frame.pack_propagate(False)
        self.card_frame.pack()
        
        self.card_label = tk.Label(self.card_frame, text="", font=("Arial", 100), bg="white")
        self.card_label.pack(expand=True)
        
        self.flip_button = tk.Button(self.card_frame, text="Flip", command=self.flip_card, font=("Arial", 14))
        self.flip_button.pack()
        
        self.next_button = tk.Button(self.card_frame, text="Next", command=self.next_card, font=("Arial", 14))
        self.next_button.pack()
        
        self.is_flipped = False
        self.current_card = None
        
        self.next_card()
    
    def next_card(self):
        self.is_flipped = False
        self.current_card = random.choice(thai_consonants)
        self.card_label.config(text=self.current_card[0])
    
    def flip_card(self):
        if self.is_flipped:
            self.card_label.config(text=self.current_card[0])
        else:
            self.card_label.config(text=self.current_card[1], font=("Arial", 20))
        self.is_flipped = not self.is_flipped

if __name__ == "__main__":
    root = tk.Tk()
    app = FlashcardApp(root)
    root.mainloop()
